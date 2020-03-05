import os
import time
import json
import threading

from selenium.webdriver import Chrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from celery import Celery
from urllib.request import urlopen
from tqdm import tqdm
from slugify import slugify


app = Celery('tmooc', broker='amqp://')
@app.task
def download(path, url):
	if not os.path.exists(path):
		with urlopen(url) as f:
			bytes_string = f.read()
		with open(path, 'wb') as f:
			f.write(bytes_string)


def goto_index():
	index_url = 'https://www.tmooc.cn/'
	driver.get(index_url)


def login():
	username = input('请输入账号：')
	password = input('请输入密码：')
	login_panel = driver.find_element_by_xpath('//a[@id="login_xxw"]')
	login_panel.click()
	#
	login_username = driver.find_element_by_xpath('//input[@id="js_account_pm"]')
	login_password = driver.find_element_by_xpath('//input[@id="js_password"]')
	login_username.clear()
	login_password.clear()
	login_username.send_keys(username)
	login_password.send_keys(password)
	#
	login_button = driver.find_element_by_xpath('//button[@id="js_submit_login"]')
	login_button.click()
	#
	retries = 0
	while retries < 50:
		try:
			login_captcha = driver.find_element_by_xpath('//div[@style!="display: none;"]/div/input[@id="js_imgcode"]')
			captcha = input('请输入验证码：')
			login_captcha.clear()
			login_captcha.send_keys(captcha)
			#
			login_button = driver.find_element_by_xpath('//button[@id="js_submit_login"]')
			login_button.click()
			break
		except:
			retries += 1


def goto_tts():
	# 判断有几个标签页打开了
	while len(driver.window_handles) == 1:
		actions = ActionChains(driver)
		#
		avatar = driver.find_element_by_xpath('//div[@class="md-2018040801-lty"]')
		actions.move_to_element(avatar)
		# 选择课程进行点击
		tts = driver.find_element_by_xpath('//li[@id="js_isshow_tts"]/a[@onclick]')
		actions.click(tts)
		#
		actions.perform()
	#
	for window_handle in driver.window_handles:
		if window_handle != driver.current_window_handle:
			driver.switch_to_window(window_handle)
	#
	driver.maximize_window()
	retries = 0
	while retries < 100:
		try:
			next_button = driver.find_element_by_xpath('//div[contains(@class, "act-1117")]/span[@class="md2017111701x-btn"]')
			next_button.click()
		except:
			retries += 1


def extract_video_page_urls():
	for stage in driver.find_elements_by_xpath('//div[contains(@class, "tree-child-box-x")]'):
		stage_name = stage.find_element_by_xpath('./div[contains(@class, "tree-child-node-x")]/p').text
		for course in stage.find_elements_by_xpath('./ul'):
			course_name = course.find_element_by_xpath('./li/span[@class="course-name-x"]').text
			for video_page in driver.find_elements_by_xpath(
				'//div[@class="video-title" and text()="{}"]'
				'/following-sibling::div[contains(@class, "video-list")]'
				'//li/div[@class="day-class"]/a'.format(course_name)
			):
				video_page_name = video_page.get_attribute('textContent')
				video_page_name = slugify(video_page_name)
				video_page_path = os.path.join(stage_name, course_name, video_page_name)
				video_page_url = video_page.get_attribute('href')
				yield video_page_path, video_page_url


def extract_video_page_pcf_urls(video_page_url):
	driver.get(video_page_url)
	#
	for i, chapter in enumerate(driver.find_elements_by_xpath('//div[@class="video-list"]/p/a')):
		pcf_name = str(i) + chapter.text + '.pcf'
		chapter.click()
		pcf_url = extract_video_pcf_url()
		yield pcf_name, pcf_url


def extract_video_pcf_url():
	while True:
		try_play_video()
		time.sleep(8)
		pcf_url = sniff_video_pcf_url()
		if pcf_url:
			return pcf_url

def sniff_video_pcf_url():
	logs = driver.get_log('performance')
	logs.reverse()
	for log in logs:
		try:
			msg = log['message']
			url = json.loads(msg)['message']['params']['response']['url']
		except:
			url = ''
		if '.pcf' in url:
			return url


def try_play_video():
	try:
		driver.execute_script('''
			videodiv = document.getElementById('videoDIV')
			embed = videodiv.getElementsByTagName("embed")[0]
			src = embed.getAttribute("src").replace("autoStart=false", "autoStart=true");
			embed.setAttribute("src", src)
		''')
	except:
		pass

def call_downloader(concurrency):
	celery_command = 'celery worker -A tmooc -c{} --loglevel=info'.format(concurrency)
	os.system(celery_command)

def call_extractor():
	pcf = dict()
	for dir_path, page_url in tqdm(paths_urls):
		for pcf_name, pcf_url in extract_video_page_pcf_urls(page_url):
			pcf_path = os.path.join(dir_path, pcf_name)
			download.delay(pcf_path, pcf_url)


if __name__ == '__main__':
	caps = DesiredCapabilities.CHROME
	caps['loggingPrefs'] = {'performance': 'ALL'}
	#
	opts = Options()
	prefs= {
		'profile.managed_default_content_settings.images': 1,
		'profile.content_settings.plugin_whitelist.adobe-flash-player': 1,
		'profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player': 1,
	}
	opts.add_experimental_option('prefs', prefs)
	#
	driver = Chrome(desired_capabilities=caps,
					chrome_options=opts)

	goto_index()
	# 登陆
	login()
	#
	goto_tts()
	#
	paths_urls = [(i, j) for i, j in extract_video_page_urls()]
	paths, urls = zip(*paths_urls)
	for path in paths:
		os.makedirs(path, exist_ok=True)

	concurrency = input('请输入最大的任务数量（不超过10个）：')

	downloader_thread = threading.Thread(target=call_downloader, args=(concurrency,))
	downloader_thread.start()

	extractor_thread = threading.Thread(target=call_extractor)
	extractor_thread.start()