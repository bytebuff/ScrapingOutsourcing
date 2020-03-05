
var dlgurl="";
var dlgtitle="";
function msgbox(spage,dltitle,width,height){
    dlgurl=spage;
    dlgtitle=dltitle;
    var sFeature='dialogWidth:'+width+'px;dialogheight:'+height+'px;center:yes;status:no;scroll:no;help:no;'
	return window.showModalDialog(webPath+"/common/modaldialog.jsp",window,sFeature);
}
function msgbox2(spage,dltitle,sFeature){
    dlgurl=spage;
    dlgtitle=dltitle;
    var sFeature=sFeature;
	return window.showModalDialog(webPath+"/common/modaldialog.jsp",window,sFeature);
}

function getPosition(element){  
	var posAry=new Array();
	var t=element.offsetTop;  var l=element.offsetLeft;  

	while(element=element.offsetParent){  
   		t+=element.offsetTop;  l+=element.offsetLeft;  
	} 
 	posAry[0]=l;
 	posAry[1]=t;
 	return posAry;
}

//document.getElementById()的快捷写法
//参数为元素id
function $() {
  var elements = new Array();
  for (var i = 0; i < arguments.length; i++) {
    var element = arguments[i];
    if (typeof element == 'string')
      element = document.getElementById(element);
    if (arguments.length == 1)
      return element;
    elements.push(element);
  }
  return elements;
}
/*****************************************CCP网站版常用方法方法***********************************************************/

/* 检查是否为邮件地址 */
function isEmail(value) {
	if (/\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*/g.test(value)) {
		return true;
	}
	return false;
}
/** 检查录入值是否为正整数 */
function isPositiveInteger(value){
	if(/^[0-9]*[1-9][0-9]*$/.test(value)){
		return true;
	}
	return false;
}



/* 检查日期是否合法，比如20080230就是错误的，不存在该日期*/
function isDate(year,month,day) {
	var t=new Date(year,month-1,day);
	year = year.substring(2,4);
	if(year != t.getYear() || month != t.getMonth()+1 || day != t.getDate())
     	  return false;
	return true;
}

//trim方法作为String对象的属性，清空字符串两侧空格
String.prototype.trim = function(){return this.replace(/(^\s*)|(\s*$)/g,'')}

//len方法作为String对象的属性，计算字符串长度
String.prototype.len = function(){return this.replace(/[^\x00-\xff]/g,'aa').length;}

/* 刷新验证码 */
function freshImg(obj) {
  var date = new Date();
  document.getElementById(obj).src = date.toString()+".check";
}

//判断是否为中文 true：中文
function isChinese(s){   
  var ret=true;   
  for(var i=0;i<s.length;i++)   
    ret=ret && (s.charCodeAt(i)>=10000);   
  return ret;   
}

//判断手机号码 11位
function phoneCheck(str) {
	if(str.len()!=11) return false;
	if(/^[0-9]*[1-9][0-9]*$/.test(str)){
		return true;
	}
	return false;
	//var regu = /^[1][3][0-9]{9}$/;
	//var regu1 = /^[1][5][8][0-9]{8}$/;
	//var regu2 = /^[1][5][0][0-9]{8}$/;
	//var re = new RegExp(regu);
	//var re1 = new RegExp(regu1);
	//var re2 = new RegExp(regu2);
	//if (re.test(str) || re1.test(str) || re2.test(str) ) {
	//	return true;
	//}
	//return false;
}

/*数据插入或文件上传时必须调用此函数检查input,TEXTAREA的内容*/
function isdanger(inputObj){
	if(inputObj==null||(inputObj.tagName!="INPUT"&&inputObj.tagName!="TEXTAREA")){
		return false;
	}
	if(inputObj.value==null)
		return false;
	/*定义正则*/
	var objRegXSS = />|<|,|\[|\]|\{|\}|\?|\/|\+|=|\||\'|\\|\"|:|;|\~|\!|\#|\*|\%|\^|\&|script|object|applet|`/i;
	var objRegFilePath = /^.*(□)|(jsp).*$/gi;
	var objRegFileName = /^\.*.(jpg)|(jpeg)|(doc)|(excel)|(docx)$/gi;
	var	re= /^insert|select|truncate|update|delete|and|or|drop|exec|net|count|:|'|"|=|;|>|<|%$/; 
	/*返回值*/
	if(inputObj.type=="file"){
		return objRegFilePath.test(inputObj.value.toLowerCase())||!objRegFileName.test(inputObj.value.toLowerCase());
	}else
	   /* 防止sql注入和js注入 */
  	   return re.test(inputObj.value.toLowerCase())||objRegXSS.test(inputObj.value.toLowerCase());
}

/**
*	根据最大字数限制，计算输入框剩余字数或超出字数,并在指定位置显示描述信息
*	fieldObj:输入框对象	
*	describeObj:描述信息(剩余字数或超出字数)显示对象
*	numInfoObj:字数信息显示对象
*	maxNum:输入框最大字数	
*/
function textCounter(fieldObj,describeObj,numInfoObj,maxNum){
	try{
		var leave = maxNum - checkLength(fieldObj.value);
		if(leave>=0){
			numInfoObj.innerHTML = leave;
			describeObj.innerHTML = "剩余字数:";
		}else{
			numInfoObj.innerHTML = -leave;
			describeObj.innerHTML = "超出字数:";
		}
	}catch(e){
		return;
	}
}

/**
  * Description  :判断参数字符串的字节长度，一个汉字占两个字节
  * Parameters  :strTemp，参数字符串
  * Return   :num
  */
function checkLength(strTemp)
{
 var i,sum;
 sum=0;
 for(i=0;i<strTemp.length;i++)
 {
  if ((strTemp.charCodeAt(i)>=0) && (strTemp.charCodeAt(i)<=255))
   sum=sum+1;
  else
   sum=sum+2;
 }
 return sum;
}
//取单选组选中按钮的值
function getRbGroupValue(rbGroup){
	for(var k=0;k<rbGroup.length;k++){
		if(rbGroup[k].checked) return rbGroup[k].value;
	}
	return null;
}
//设置单选按钮组选中
function setRbGroupChecked(grpName,value){
	var arr = document.getElementsByName(grpName);
	for(var i=0;i<arr.length;i++){
		if(arr[i].value == value){
			arr[i].checked = true;
			return;
		}
	}
}