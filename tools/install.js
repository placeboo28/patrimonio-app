<script>(function(){
if (window.matchMedia && matchMedia('(display-mode: standalone)').matches) return;
function show(){
  if (!window.__gpDP || !document.body || document.getElementById('gp-inst')) return;
  var b=document.createElement('button'); b.id='gp-inst'; b.type='button'; b.textContent='⬇ Instalar app';
  b.style.cssText='position:fixed;left:50%;bottom:calc(18px + env(safe-area-inset-bottom,0px));transform:translateX(-50%);z-index:99999;padding:13px 24px;border:none;border-radius:26px;background:#1F4E79;color:#fff;font:600 15px system-ui,sans-serif;box-shadow:0 6px 18px rgba(0,0,0,.28);cursor:pointer';
  b.onclick=function(){ var p=window.__gpDP; if(!p) return; p.prompt(); p.userChoice.then(function(){ window.__gpDP=null; b.remove(); }); };
  document.body.appendChild(b);
}
window.addEventListener('beforeinstallprompt', function(e){ e.preventDefault(); window.__gpDP=e; show(); });
window.addEventListener('appinstalled', function(){ window.__gpDP=null; var b=document.getElementById('gp-inst'); if(b) b.remove(); });
if (document.readyState==='loading') document.addEventListener('DOMContentLoaded', show); else show();
})();</script>
