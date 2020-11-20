function toggleBlur(){
    if (document.getElementById('hidden').classList[0] == "blur"){
        document.getElementById('hidden').classList.remove('blur')
        document.getElementById('show').classList.add('toggled')
    } else{
        document.getElementById('hidden').classList.add('blur')
        document.getElementById('show').classList.remove('toggled')
    }
}
alert("Podgląd layoutu, niepodpięte pod flaska")