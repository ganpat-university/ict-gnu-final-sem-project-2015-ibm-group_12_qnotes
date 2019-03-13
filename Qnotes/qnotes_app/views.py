from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.contrib.auth import logout as auth_logout
import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["Qnotes"]
mycol=mydb["extranotes"]
mycol1=mydb["counters"]
mycol2=mydb["todo"]
mycol3=mydb["todocounters"]
mycol4=mydb["users"]
mycol5=mydb["usercounters"]
list_todo = []


def welcome(request):
	return redirect("/index")

def index(request):
	return render(request,"index.html")

def logout(request):
    auth_logout(request)
    return redirect('/index')


def show_notes(request):
	uname = str(request.user)
	if(uname != "AnonymousUser"):
		fname = str(request.user.first_name)
		lname = str(request.user.last_name)
		email = str(request.user.email)
		print("email : ",email)
		data1=mycol4.find({"uname":uname,"email":email}).count()
		if(data1 == 0):
			seq=mycol5.find_one({"id" : "uid"})
			y=seq['sequence_value']
			y=int(y)
			y=y+1
			myquery = {'id':"uid"}
			newvalues = { "$set": { "sequence_value": y } }
			mycol5.update_one(myquery, newvalues)
			data1={
			'id':y,
			'fname':fname,
			'lname':lname,
			'uname':uname,
			'email':email,
			}
			mycol4.insert_one(data1)
	data=mycol.find({"author":uname})
	return render(request,"notes.html",{"data":data,"n_status":1})


def create_notes(request):
	title=request.POST.get('title')
	content=request.POST.get('content')
	user=str(request.user)
	seq=mycol1.find_one({"id" : "noteid"})
	y=seq['sequence_value']
	y=int(y)
	y=y+1
	myquery = {'id':"noteid"}
	newvalues = { "$set": { "sequence_value": y } }
	mycol1.update_one(myquery, newvalues)
	data={
	'id':y,
	'title':title,
	'content':content,
	'author': user,
	'fav_flag':0,
	'arc_flag':0,
	'note_colour':'#cfc'
	}
	mycol.insert_one(data)
	data=mycol.find({"author":user})
	return render(request,"notes.html",{"data":data,"n_status":1})

def goto_search_note(request):
	return render(request,"search.html",{"s_status":1})

def search_note(request):
	searchstr=request.POST.get("title")
	cb=request.POST.get("checkbox1")
	user=str(request.user)
	#print("check box value : ",cb)
	temp=[]
	

	if(cb == "on"):
		print("check box value : ",cb)
		data=mycol.find({"author":user,"fav_flag":1})
		count=mycol.find({"author":user,"fav_flag":1}).count()
		for i in range(count):
			stemp= data[i].get('title')
			if(stemp.__contains__(searchstr)):
				temp.append(data[i])
		print(temp)

	else:
		print("check box value : ",cb)
		data=mycol.find({"author":user,"fav_flag":0,"arc_flag":0})
		count=mycol.find({"author":user,"fav_flag":0,"arc_flag":0}).count()
		print(data)
		for i in range(count):
			stemp= data[i].get('title')
			if(stemp.__contains__(searchstr)):
				temp.append(data[i])
		print(temp)
	return render(request,"search.html",{"data":temp,"s_status":1})


def colour_change1(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.update_one({"id":nid}, { "$set": {"note_colour":"#ffc" }})
	data=mycol.find({"author":user})
	return render(request,"notes.html",{"data":data,"n_status":1})


def colour_change2(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.update_one({"id":nid}, { "$set": {"note_colour":"#cfc" }})
	data=mycol.find({"author":user})
	return render(request,"notes.html",{"data":data,"n_status":1})


def colour_change3(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.update_one({"id":nid}, { "$set": {"note_colour":"#aecbfa" }})
	data=mycol.find({"author":user})
	return render(request,"notes.html",{"data":data,"n_status":1})


def colour_change4(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.update_one({"id":nid}, { "$set": {"note_colour":"#d7aefb" }})
	data=mycol.find({"author":user})
	return render(request,"notes.html",{"data":data,"n_status":1})


def colour_change5(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.update_one({"id":nid}, { "$set": {"note_colour":"#ccebff" }})
	data=mycol.find({"author":user})
	return render(request,"notes.html",{"data":data,"n_status":1})


def colour_change6(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.update_one({"id":nid}, { "$set": {"note_colour":"#f28b82" }})
	data=mycol.find({"author":user})
	return render(request,"notes.html",{"data":data,"n_status":1})


def colour_change7(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.update_one({"id":nid}, { "$set": {"note_colour":"#cccccc" }})
	data=mycol.find({"author":user})
	return render(request,"notes.html",{"data":data,"n_status":1})


def colour_change8(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.update_one({"id":nid}, { "$set": {"note_colour":"#fdcfe8" }})
	data=mycol.find({"author":user})
	return render(request,"notes.html",{"data":data,"n_status":1})

def edit_note(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	myquery={"id":nid,"author":user}
	data=mycol.find_one(myquery)
	return render(request,"edit_note.html",{"data":data,"n_status":1})


def update_note(request):
	user=str(request.user)
	nid=request.POST.get('id')
	nid=int(nid)
	etitle=request.POST.get('etitle')
	econtent=request.POST.get('econtent')
	mycol.update_one({"id":nid}, { "$set": {"title":etitle, "content":econtent }})
	data=mycol.find({"author":user})
	return render(request,"notes.html",{"data":data,"n_status":1})


def delete_note(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.delete_one({"id":nid}) 
	data=mycol.find({"author":user})
	return render(request,"notes.html",{"data":data,"n_status":1})


def fav_note(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.update_one({"id":nid}, { "$set": {"fav_flag":1 }})
	favdata=mycol.find({"fav_flag" : 1,"author":user})	
	return render(request,"favourites.html",{'favdata':favdata,"f_status":1})



def unfav(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.update_one({"id":nid}, { "$set": {"fav_flag":0 }})
	favdata=mycol.find({"author":user})	
	return render(request,"notes.html",{'data':favdata,"n_status":1})


def show_fav(request):
	user=str(request.user)
	favdata=mycol.find({"fav_flag" : 1,"author":user,"arc_flag":0})
	return render(request,"favourites.html",{'favdata':favdata,"f_status":1})


def archive_note(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.update_one({"id":nid}, { "$set": {"arc_flag":1 }})
	arcdata=mycol.find({"author":user})
	return render(request,"notes.html",{'data':arcdata,"n_status":1})


def undo_archive(request,id):
	user=str(request.user)
	#arc=request.POST.get('arc_flag')
	#fav=request.POST.get('fav_flag')
	#title=request.POST.get("title")
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol.update_one({"id":nid}, { "$set": {"arc_flag":0 }})
	arcdata=mycol.find({"author":user})
	#print("arc :: ",arc," fav :: ",fav," title :: ",title)
	#if(arc==0 and fav==1):
	#	return render(request,"favourites.html",{'data':arcdata})
	return render(request,"notes.html",{'data':arcdata,"n_status":1})


def show_archive(request):
	user=str(request.user)
	arcdata=mycol.find({"arc_flag" : 1,"author":user})
	return render(request,"archive.html",{'arcdata':arcdata,"a_status":1})


def show_todo(request):
	user=str(request.user)
	temp={"0"}
	dic={}
	fl=[]
	main_id=[]
	for i in mycol2.find({},{"_id":0,"id":1,"author":1}):
		#print(i)
		temp.add(i.get('id'))
	temp.remove("0")
	for x in temp:
		t1=[]
		main_id.append(x)
		for i in mycol2.find({"id":x,"author":user}):
			#print(i)
			t1.append(i)
		fl.append(t1)
	
	return render(request,'todo_list.html',{'data':fl,'mainid':main_id,"t_status":1})


def goto_todo(request):
	user=str(request.user)
	return render(request,'create_todo.html',{"t_status":1})


def create_todo(request):
	user=str(request.user)
	global list_todo
	con=request.POST.get('todocont')
	list_todo.append(con)
	#print(con)
	data=mycol2.find({"author":user})
	
	return render(request,"create_todo.html",{'data':list_todo,"t_status":1})


def insert_todo(request):
	user=str(request.user)
	seq=mycol1.find_one({"id" : "noteid"})
	y=seq['sequence_value']
	y=int(y)
	y=y+1
	myquery = {'id':"noteid"}
	newvalues = { "$set": { "sequence_value": y } }
	mycol1.update_one(myquery, newvalues)
	for td in range(len(list_todo)):
		seq1=mycol3.find_one({"id" : "tid"})
		q=seq1['sequence_value']
		q=int(q)
		q=q+1	
		myquery = {'id':"tid"}
		newvalues = { "$set": { "sequence_value": q } }
		mycol3.update_one(myquery, newvalues)
		data={  'id':y,
				'tid':q,
				"content":list_todo[td],
				"author":user,
			 }
		mycol2.insert_one(data)
	list_todo.clear()
	temp={"0"}
	dic={}
	fl=[]
	for i in mycol2.find({},{"_id":0,"id":1,"author":1}):
		temp.add(i.get('id'))
	temp.remove("0")
	for x in temp:
		t1=[]
		for i in mycol2.find({"id":x,"author":user}):
			#print(i)
			t1.append(i)
		fl.append(t1)
	
	return render(request,'todo_list.html',{'data':fl,"t_status":1})
	

def add_todogoto(request,id):
	user=str(request.user)
	path=request.get_full_path()
	#print(path)
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	myquery={"id":nid}
	
	return render(request,"update_todo.html",{"data":myquery,"t_status":1})


def update_todo(request):
	user=str(request.user)
	nid=request.POST.get('idtodo')
	nid=int(nid)
	content=request.POST.get('todocont')
	seq1=mycol3.find_one({"id" : "tid"})
	q=seq1['sequence_value']
	q=int(q)
	q=q+1	
	myquery = {'id':"tid"}
	newvalues = { "$set": { "sequence_value": q } }
	mycol3.update_one(myquery, newvalues)
	data={'id':nid,'tid':q,"content":content,"author":user}
	mycol2.insert_one(data)		
	temp={"0"}
	dic={}
	fl=[]
	for i in mycol2.find({},{"_id":0,"id":1,"author":1}):
		temp.add(i.get('id'))
	temp.remove("0")
	for x in temp:
		t1=[]
		for i in mycol2.find({"id":x,"author":user}):
			#print(i)
			t1.append(i)
		fl.append(t1)
	
	return render(request,'todo_list.html',{'data':fl,"t_status":1})


def delete_todo(request,id):
	user=str(request.user)
	path=request.get_full_path()
	path=path.split('/')
	nid=path[2]
	nid=int(nid)
	mycol2.delete_one({"tid":nid})
	temp={"0"}
	dic={}
	fl=[]
	for i in mycol2.find({},{"_id":0,"id":1,"author":1}):
		temp.add(i.get('id'))
	temp.remove("0")
	for x in temp:
		t1=[]
		for i in mycol2.find({"id":x,"author":user}):
			#print(i)
			t1.append(i)
		fl.append(t1)
	
	return render(request,'todo_list.html',{'data':fl,"t_status":1})