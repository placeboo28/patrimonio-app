#!/usr/bin/env python3
"""Genera la app de consulta (sin cifrar) con los datos embebidos.
Uso: build_snapshot.py <index.html del artifact> <snapshot.json> <salida.html>"""
import sys, json, time
src, snap, out = sys.argv[1:4]
html = open(src, encoding="utf8").read()
data = json.load(open(snap, encoding="utf8"))
fecha = time.strftime("%d/%m/%Y %H:%M", time.localtime())
shim = """<script>
window.__SNAPSHOT={fecha:%s};
(function(){
  const D=%s;
  const db={collection:c=>({
    onSnapshot:(cb)=>{setTimeout(()=>cb({docs:(D[c]||[]).map(d=>({id:d.id,data:()=>d.data}))}),0);return ()=>{}},
    doc:()=>({set:async()=>{throw {code:"invalid_argument"}},update:async()=>{throw {code:"invalid_argument"}},delete:async()=>{throw {code:"invalid_argument"}}}),
    add:async()=>{throw {code:"invalid_argument"}}})};
  const dl={save:async({filename,data})=>{const u=URL.createObjectURL(data);const a=document.createElement("a");a.href=u;a.download=filename;document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(u),4000)}};
  window.claude={use:async n=>n==="db"?db:n==="downloads"?dl:null};
})();
</script>
""" % (json.dumps(fecha), json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
i = html.find("<script src=")
html = html[:i] + shim + html[i:]
html = html.replace('<title>Gestión Patrimonio</title>', '<title>Gestión Patrimonio</title>\n<meta name="robots" content="noindex,nofollow">', 1)
open(out, "w", encoding="utf8").write(html)
print("OK", out, len(html), "bytes ·", fecha)
