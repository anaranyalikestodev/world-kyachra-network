const socket=io()

let user=null
let session=null

function join(){

user=document.getElementById("user").value
session=document.getElementById("session").value
const password=document.getElementById("password").value

socket.emit("chat_join",{user,password,session})

}

socket.on("chat_joined",()=>{

document.getElementById("login").style.display="none"
document.getElementById("chat").style.display="flex"

})


socket.on("chat_message",(msg)=>{

const box=document.getElementById("chatbox")

const div=document.createElement("div")

div.classList.add("message")

if(msg.user===user)
div.classList.add("self")
else
div.classList.add("other")

div.innerText=msg.user+": "+msg.text

box.appendChild(div)

box.scrollTop=box.scrollHeight


setTimeout(()=>{
div.remove()
},60000)

})


socket.on("error",(e)=>{

alert(e.msg)

})


function send(){

const text=document.getElementById("msg").value

if(text.trim()==="") return

socket.emit("chat_message",{user,session,text})

document.getElementById("msg").value=""

}

socket.on("chat_joined",()=>{
    document.getElementById("login").classList.add("d-none")
    document.getElementById("chat").classList.remove("d-none")
})