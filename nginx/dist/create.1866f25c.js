parcelRequire=function(e,r,t,n){var i,o="function"==typeof parcelRequire&&parcelRequire,u="function"==typeof require&&require;function f(t,n){if(!r[t]){if(!e[t]){var i="function"==typeof parcelRequire&&parcelRequire;if(!n&&i)return i(t,!0);if(o)return o(t,!0);if(u&&"string"==typeof t)return u(t);var c=new Error("Cannot find module '"+t+"'");throw c.code="MODULE_NOT_FOUND",c}p.resolve=function(r){return e[t][1][r]||r},p.cache={};var l=r[t]=new f.Module(t);e[t][0].call(l.exports,p,l,l.exports,this)}return r[t].exports;function p(e){return f(p.resolve(e))}}f.isParcelRequire=!0,f.Module=function(e){this.id=e,this.bundle=f,this.exports={}},f.modules=e,f.cache=r,f.parent=o,f.register=function(r,t){e[r]=[function(e,r){r.exports=t},{}]};for(var c=0;c<t.length;c++)try{f(t[c])}catch(e){i||(i=e)}if(t.length){var l=f(t[t.length-1]);"object"==typeof exports&&"undefined"!=typeof module?module.exports=l:"function"==typeof define&&define.amd?define(function(){return l}):n&&(this[n]=l)}if(parcelRequire=f,i)throw i;return f}({"mfDx":[function(require,module,exports) {
var t=window.location.hostname,e="1337",n=function(){return function(t,e){this.vector=t,this.id_graph=e}}(),o=document.getElementById("add"),r=document.getElementById("create_vector"),a=document.getElementById("target"),i=document.getElementById("id_graph"),c=document.getElementById("status_request");function u(){for(var t=[],e=0,n=Array.prototype.slice.call(a.getElementsByTagName("input"));e<n.length;e++){var o=n[e];t.push(Number(o.value))}return t}function d(){a.insertAdjacentHTML("beforeend","<input id="+a.getElementsByTagName("input").length+">")}function s(){var n={vector:u()};fetch("http://"+t+":"+e+"/graph/",{method:"POST",headers:{Accept:"application/json, text/plain","Content-Type":"application/json;charset=UTF-8"},body:JSON.stringify(n)}).then(function(t){return console.log(t),t.json().then(function(e){return{status:t.status,body:e}})}).then(function(t){200==t.status?i.innerHTML=t.body.id:404==t.status&&(c.innerHTML="Not Found")})}o.addEventListener("click",d),r.addEventListener("click",s);
},{}]},{},["mfDx"], null)
//# sourceMappingURL=/create.1866f25c.js.map