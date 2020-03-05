var dlgurl="";
var dlgtitle="";
function msgbox(spage,dltitle,width,height){
    dlgurl=spage;
    dlgtitle=dltitle;
    var sFeature='dialogWidth:'+width+'px;dialogheight:'+height+'px;center:yes;status:no;scroll:no;help:no;'
	return window.showModalDialog(webPath+"/cicpa/common/modaldialog.jsp",window,sFeature);
}
function msgbox_base(spage,dltitle,width,height){
    dlgurl=spage;
    dlgtitle=dltitle;
    var sFeature='dialogWidth:'+width+'px;dialogheight:'+height+'px;center:yes;status:no;scroll:no;help:no;'
	return window.showModalDialog(webPath+"/cicpa/common/modaldialog_base.jsp",window,sFeature);
}
function setColor(id){
	var oTable = document.getElementById(id);
	for(var i=1;i<oTable.rows.length;i++){
		if(i%2==0) oTable.rows[i].className='tabbak';
	}
}
/*************************************导出开始********************************************/
/**
*截取浮点数的NUM位有效小数
*@value 传入参数
*@num 小数位
*@return 返回截取后的值(如果传入的不是浮点数则返回原数)
*/
function roundFloat(value,num){
	var vStr = value.toString();
	var reg = new RegExp("^(\\d+\\.\\d{"+num+"})\\d*$");
	if(reg.test(vStr)){
		var fV = vStr.replace(reg,"$1");
		return parseFloat(fV).toFixed(num);  
	} 
	return parseFloat(value);
}   
 
//主要要进行的操作是计算行高和列宽，只需要计算最外层table的列宽即可 
//如果有嵌套的情况(嵌套表格的行高以内部表格为标准，列宽则以第一个表格为标准) 
function exportExcel(tableid) {//整个表格拷贝到EXCEL中   
	//检索浏览器  
	if(navigator.userAgent.indexOf("MSIE")<0){  
	    alert('请用ie浏览器进行表格导出');  
	    return;  
	}
	var curTbl = document.getElementById(tableid);   
	var oExcelApp = null;   
	//创建Excel应用程序对象oExcelApp
	try {  
	    oExcelApp = GetObject("", "Excel.Application");  
	}  
	catch (E) {  
	    try {  
	        oExcelApp = new ActiveXObject("Excel.Application");  
	    }  
	    catch (E2) {  
	        alert("请确认已经执行了如下操作:\n1.您的电脑已经安装Microsoft Excel软件！。\n2.浏览器中Internet选项=>安全=>自定义级别中已经设置\"允许运行ActiveX控件\"。");  
	        return;  
	    }  
	}
	
	//新增excel工作簿   
	var oExcelBook = oExcelApp.Workbooks.Add();   
	 //获取workbook对象   
	var oSheet = oExcelBook.ActiveSheet;   
	      
	//在此进行样式控制 
	var letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];
	var trows = curTbl.rows;
	    
	//判断第一个表格行内是否有嵌套表格，如果有则以第一个嵌套表格为标准(目前只处理最外层表格只有一个单元格的情况)
	if(trows.length > 0 && trows[0].cells.length >0){
		if(trows[0].cells[0].firstChild.nodeName=='TABLE' && trows[0].cells.length!=1){
			alert('导出表格不符合规范，暂时无法处理！');
			return;
		}
		if(trows[0].cells[0].firstChild.nodeName=='TABLE'){
			var innerTab = trows[0].cells[0].firstChild;
			var inRows = innerTab.rows;
			var maxCellsIndex = 0;
			var maxColLength = 0;
			//设置第一个内部表格行高
			for(var i=0;i<inRows.length;i++){
				var cells = inRows[i].cells;
				if(cells.length > maxColLength){
					maxColLength = cells.length;
					maxCellsIndex = i;
				} 
				oSheet.Rows((i+1)+":"+(i+1)).RowHeight=roundFloat(inRows[i].clientHeight*3/4,2);
			}			
			//设置列宽
			var maxCells = inRows[maxCellsIndex].cells;
			for(var j=0;j<maxCells.length;j++){
				oSheet.Columns(letters[j]+":"+letters[j]).ColumnWidth = roundFloat((maxCells[j].clientWidth/80)*10,2);
			}
			//设置其它表格行高
		}
		else{
			var maxCellsIndex = 0;
			var maxColLength = 0;
			//设置行高
			for(var i=0;i<trows.length;i++){
				var cells = trows[i].cells;
				if(cells.length > maxColLength){
					maxColLength = cells.length;
					maxCellsIndex = i;
				} 
				oSheet.Rows((i+1)+":"+(i+1)).RowHeight=roundFloat(trows[i].clientHeight*3/4,2);
			}
			//设置列宽
			var maxCells = trows[maxCellsIndex].cells;
			for(var j=0;j<maxCells.length;j++){
				oSheet.Columns(letters[j]+":"+letters[j]).ColumnWidth = roundFloat((maxCells[j].clientWidth/80)*10,2);
			}			
		}
	}
	oSheet.Rows(1).HorizontalAlignment=3;     
	
	var sel = document.body.createTextRange(); //激活当前sheet   
	sel.moveToElementText(curTbl); //把表格中的内容移到TextRange中  
	//sel.select();  //全选TextRange中内容   
	sel.execCommand("Copy"); //复制TextRange中内容   
	oSheet.Paste(); //粘贴到活动的EXCEL中   
	oExcelApp.Visible = true; //设置excel可见属性  
	  
	oSheet.Application.Quit(); //结束当前进程  
	
	window.opener=null;  
	window.close(); //关闭当前窗口
}   
/*************************************导出结束********************************************/