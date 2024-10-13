$(document).ready(function () {
    $('#gemini-form').submit(function (event) {
      event.preventDefault(); // Formun varsayılan gönderimini engelle
      
      var userInput = $('#inputText').val(); // Kullanıcının girdiği metni al
      $('#response').append('<div class="user-message">Siz: ' + userInput + '</div>'); // Kullanıcı mesajını ekle
      $('#inputText').val(''); // Girdi alanını temizle

      // POST isteği ile kullanıcı girdiğini sunucuya gönder
      $.post('/chat', { user_input: userInput }, function (data) {
        $('#response').append('<div class="bot-response">WexBot: ' + data.response + '</div>'); // Bot yanıtını ekle
        $('#response').scrollTop($('#response')[0].scrollHeight); // Yanıtın görünmesi için kaydır
      });
    });

    $('#mesaj').keypress(function (e) {
      if (e.which === 13) {
        $('#gonder').click();
      }
    });
  });
document.getElementById("gonder").addEventListener("click",function(){var m=document.getElementById("mesaj").value;if(m.trim()!==""){var c=document.createElement("div");c.textContent=m;document.querySelector(".kullanici-container").appendChild(c);document.getElementById("mesaj").value="";}});var i=document.getElementById("mesaj");var g=document.getElementById("gonder");i.addEventListener("input",function(){if(i.value.trim()!==""){g.classList.remove("gonder-hidden");g.classList.add("gonder-visible");}else{g.classList.remove("gonder-visible");g.classList.add("gonder-hidden");}});i.addEventListener("keyup",function(){if(i.value.trim()===""){g.classList.remove("gonder-visible");g.classList.add("gonder-hidden");}});document.querySelector(".mikrofon").addEventListener("click",function(){navigator.mediaDevices.getUserMedia({audio:true}).then(function(s){var a=document.createElement("audio");a.srcObject=s;a.play();}).catch(function(e){console.error('Mikrofon erişimi alınamadı: '+e);});});fetch('https://ipinfo.io/json').then(r=>r.json()).then(d=>{var il=d.city;var ulke=d.country;var k=il+', '+ulke;document.getElementById("konumBilgisi").textContent=k;}).catch(e=>{console.error('Hata:',e);document.getElementById("konumBilgisi").textContent="Konum bilgisi alınamadı.";});document.getElementById("mesaj").addEventListener("input",function(){if(this.value.trim()!==""){document.getElementById("gonder").style.left="0";document.getElementById("gonder").style.display="inline-block";}else{document.getElementById("gonder").style.left="-100px";}});document.addEventListener("DOMContentLoaded",function(){function sendMessage(){var h=document.querySelector('.hosgeldin');if(h){h.style.display='none';}}document.getElementById("gonder").addEventListener("click",sendMessage);});document.body.style.userSelect='none';document.addEventListener('DOMContentLoaded',function(){const i=document.querySelector('.inputcevre input[type="text"]');const ic=document.querySelector('.inputcevre');i.addEventListener('focus',function(){ic.style.backgroundColor='#282a2c';});i.addEventListener('blur',function(){ic.style.backgroundColor='#1e1f20';});});var m=document.querySelector(".menu");var s=document.querySelector(".sidenav");var o=false;m.addEventListener("click",function(){if(o){closeNav();}else{openNav();}o=!o;});function openNav(){s.classList.remove("sidenav-closed");s.classList.add("sidenav-open");}function closeNav(){s.classList.remove("sidenav-open");s.classList.add("sidenav-closed");}
