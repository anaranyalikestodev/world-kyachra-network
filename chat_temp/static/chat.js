const socket = io()

let user = null
let session = null
const urlParams=new URLSearchParams(window.location.search)

if(urlParams.has("session")){
document.getElementById("session").value=urlParams.get("session")
}

function join(){
    
history.replaceState(null,"","?session="+session)
user=document.getElementById("user").value

session=document.getElementById("session").value
const password=document.getElementById("password").value

socket.emit("chat_join",{user,password,session})

}


socket.on("chat_joined",()=>{

document.getElementById("login").classList.add("d-none")
document.getElementById("chat").classList.remove("d-none")

})


socket.on("chat_message",(msg)=>{

const box=document.getElementById("chatbox")

const wrapper=document.createElement("div")

wrapper.classList.add("message")

if(msg.user===user)
wrapper.classList.add("self")
else
wrapper.classList.add("other")


const name=document.createElement("div")
name.className="msg-name"
name.innerText=msg.user


const text=document.createElement("div")
text.className="msg-text"
text.innerText=msg.text


const time=document.createElement("div")
time.className="msg-time"

const date=new Date(msg.time*1000)
const ist=date.toLocaleTimeString("en-IN",{timeZone:"Asia/Kolkata",hour12:false})

time.innerText=ist


wrapper.appendChild(name)
wrapper.appendChild(text)
wrapper.appendChild(time)

box.appendChild(wrapper)

box.scrollTop=box.scrollHeight


setTimeout(()=>{
wrapper.remove()
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


document.getElementById("msg").addEventListener("keypress",function(e){
if(e.key==="Enter"){
send()
}
})