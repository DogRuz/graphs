parcelRequire=function(e,r,t,n){var i,o="function"==typeof parcelRequire&&parcelRequire,u="function"==typeof require&&require;function f(t,n){if(!r[t]){if(!e[t]){var i="function"==typeof parcelRequire&&parcelRequire;if(!n&&i)return i(t,!0);if(o)return o(t,!0);if(u&&"string"==typeof t)return u(t);var c=new Error("Cannot find module '"+t+"'");throw c.code="MODULE_NOT_FOUND",c}p.resolve=function(r){return e[t][1][r]||r},p.cache={};var l=r[t]=new f.Module(t);e[t][0].call(l.exports,p,l,l.exports,this)}return r[t].exports;function p(e){return f(p.resolve(e))}}f.isParcelRequire=!0,f.Module=function(e){this.id=e,this.bundle=f,this.exports={}},f.modules=e,f.cache=r,f.parent=o,f.register=function(r,t){e[r]=[function(e,r){r.exports=t},{}]};for(var c=0;c<t.length;c++)try{f(t[c])}catch(e){i||(i=e)}if(t.length){var l=f(t[t.length-1]);"object"==typeof exports&&"undefined"!=typeof module?module.exports=l:"function"==typeof define&&define.amd?define(function(){return l}):n&&(this[n]=l)}if(parcelRequire=f,i)throw i;return f}({"sR5P":[function(require,module,exports) {
var t=this&&this.__awaiter||function(t,e,n,r){return new(n||(n=Promise))(function(o,u){function a(t){try{s(r.next(t))}catch(e){u(e)}}function i(t){try{s(r.throw(t))}catch(e){u(e)}}function s(t){var e;t.done?o(t.value):(e=t.value,e instanceof n?e:new n(function(t){t(e)})).then(a,i)}s((r=r.apply(t,e||[])).next())})},e=this&&this.__generator||function(t,e){var n,r,o,u,a={label:0,sent:function(){if(1&o[0])throw o[1];return o[1]},trys:[],ops:[]};return u={next:i(0),throw:i(1),return:i(2)},"function"==typeof Symbol&&(u[Symbol.iterator]=function(){return this}),u;function i(u){return function(i){return function(u){if(n)throw new TypeError("Generator is already executing.");for(;a;)try{if(n=1,r&&(o=2&u[0]?r.return:u[0]?r.throw||((o=r.return)&&o.call(r),0):r.next)&&!(o=o.call(r,u[1])).done)return o;switch(r=0,o&&(u=[2&u[0],o.value]),u[0]){case 0:case 1:o=u;break;case 4:return a.label++,{value:u[1],done:!1};case 5:a.label++,r=u[1],u=[0];continue;case 7:u=a.ops.pop(),a.trys.pop();continue;default:if(!(o=(o=a.trys).length>0&&o[o.length-1])&&(6===u[0]||2===u[0])){a=0;continue}if(3===u[0]&&(!o||u[1]>o[0]&&u[1]<o[3])){a.label=u[1];break}if(6===u[0]&&a.label<o[1]){a.label=o[1],o=u;break}if(o&&a.label<o[2]){a.label=o[2],a.ops.push(u);break}o[2]&&a.ops.pop(),a.trys.pop();continue}u=e.call(t,a)}catch(i){u=[6,i],r=0}finally{n=o=0}if(5&u[0])throw u[1];return{value:u[0]?u[1]:void 0,done:!0}}([u,i])}}},n=window.location.hostname,r="1337",o=document.getElementById("search_click"),u=document.getElementById("status_request"),a={1:"add",2:"mul",3:"subtraction",4:"division"};function i(o){return t(this,void 0,void 0,function(){return e(this,function(t){switch(t.label){case 0:return[4,fetch("http://"+n+":"+r+"/graph/?id="+o).then(function(t){return t.json().then(function(e){return{status:t.status,body:e}})}).then(function(t){return"["+t.body.vector.join(",")+"]"})];case 1:return[2,t.sent()]}})})}function s(o){return t(this,void 0,void 0,function(){return e(this,function(t){switch(t.label){case 0:return[4,fetch("http://"+n+":"+r+"/operation/?id="+o).then(function(t){return t.json().then(function(e){return{status:t.status,body:e}})}).then(function(t){return t.body.operation_id})];case 1:return[2,t.sent()]}})})}function c(){var o=this,c=document.getElementById("graph").value;fetch("http://"+n+":"+r+"/parent/?id="+c).then(function(t){return t.json().then(function(e){return{status:t.status,body:e}})}).then(function(n){return t(o,void 0,void 0,function(){var t,r,o,c,l,f,d,h,b,p,v,y,m,w,g,k,N,_,E,j;return e(this,function(e){switch(e.label){case 0:if(200!=n.status)return[3,10];u.innerHTML="Success",t=new Map,r=[],o=0,c=Object.entries(n.body.connections),e.label=1;case 1:return o<c.length?(l=c[o],f=l[0],d=l[1],h=parseInt(f),null!=t.get(h)?[3,8]:[4,i(h)]):[3,9];case 2:return b=e.sent(),t.set(h,b),[4,s(h)];case 3:for(m in p=e.sent(),v=99999+p,t.set(v,a[p]),r.push({from:v,to:h}),y=[],d)y.push(m);w=0,e.label=4;case 4:return w<y.length?(g=y[w],null!=t.get(d[g])?[3,6]:[4,i(d[g])]):[3,8];case 5:k=e.sent(),t.set(d[g],k),e.label=6;case 6:r.push({from:d[g],to:v}),e.label=7;case 7:return w++,[3,4];case 8:return o++,[3,1];case 9:return N=new vis.DataSet,Array.from(t,function(t){var e=t[0],n=t[1];N.add({id:e,label:n})}),_=document.getElementById("mynetwork"),E={nodes:N,edges:r},j={},new vis.Network(_,E,j),[3,11];case 10:404==n.status&&(u.innerHTML="Not Found"),e.label=11;case 11:return[2]}})})})}o.addEventListener("click",c);var l=new vis.DataSet([{id:1,label:"Node 1"},{id:2,label:"Node 2"},{id:3,label:"Node 3"},{id:4,label:"Node 4"},{id:5,label:"Node 5"}]),f=[{from:1,to:3},{from:1,to:2},{from:2,to:4},{from:2,to:5},{from:3,to:3}];
},{}]},{},["sR5P"], null)
//# sourceMappingURL=/visualize.ec2e7a9a.js.map