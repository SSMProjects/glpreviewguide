/* GLP1ReviewGuide home templates: shared motion layer.
   GSAP 3.12 + ScrollTrigger + MotionPathPlugin, Lenis 1.1 smooth scroll.
   Everything here is progressive: without the libraries (or with reduced motion) the page shows its final state. */
(function(){
 var d=document,H=d.documentElement,W=window;
 W.__mo=true;
 var $=function(s,r){return [].slice.call((r||d).querySelectorAll(s));};
 var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
 var finePointer=matchMedia('(hover:hover) and (pointer:fine)').matches;
 function showAll(){$('[data-r],[data-split]').forEach(function(e){e.classList.add('in');});}
 if(!W.gsap||!W.ScrollTrigger||reduce){showAll();d.dispatchEvent(new Event('motion:off'));return;}
 var g=W.gsap,ST=W.ScrollTrigger;
 g.registerPlugin(ST);if(W.MotionPathPlugin)g.registerPlugin(W.MotionPathPlugin);
 H.classList.add('mo');
 var OUT='expo.out';

 /* Lenis: inertial scrolling, driven by GSAP's ticker so ScrollTrigger stays in sync */
 var lenis=null;
 if(W.Lenis){
  lenis=new W.Lenis({lerp:0.1,smoothWheel:true});
  lenis.on('scroll',ST.update);
  g.ticker.add(function(t){lenis.raf(t*1000);});
  g.ticker.lagSmoothing(0);
  W.__lenis=lenis;
 }
 $('a[href^="#"]').forEach(function(a){a.addEventListener('click',function(e){
  var id=a.getAttribute('href');if(id.length<2)return;var t=d.querySelector(id);if(!t)return;
  e.preventDefault();
  if(lenis)lenis.scrollTo(t,{offset:-76,duration:1.2});else t.scrollIntoView({behavior:'smooth'});
  history.replaceState(null,'',id);
 });});

 /* split text: words rise out of a mask (React Bits "SplitText", rebuilt with GSAP) */
 function split(el){
  var out=[];
  (function walk(node){
   [].slice.call(node.childNodes).forEach(function(n){
    if(n.nodeType===3){
     var parts=n.textContent.split(/(\s+)/),f=d.createDocumentFragment();
     parts.forEach(function(p){
      if(!p)return;
      if(/^\s+$/.test(p)){f.appendChild(d.createTextNode(p));return;}
      var w=d.createElement('span');w.className='sw';var i=d.createElement('span');i.textContent=p;w.appendChild(i);f.appendChild(w);out.push(i);
     });
     n.parentNode.replaceChild(f,n);
    }else if(n.nodeType===1&&n.tagName!=='BR'){
     if(n.classList.contains('frame')||n.hasAttribute('data-unit')){
      var w2=d.createElement('span');w2.className='sw';n.parentNode.insertBefore(w2,n);w2.appendChild(n);out.push(n);
     }else walk(n);
    }
   });
  })(el);
  return out;
 }
 $('[data-split]').forEach(function(el){
  var words=split(el),hero=el.closest('.hero');
  g.set(el,{opacity:1});
  var tw={yPercent:115,rotate:4,duration:1.1,ease:OUT,stagger:0.06};
  if(hero){g.from(words,Object.assign(tw,{delay:0.15}));}
  else{g.from(words,Object.assign(tw,{scrollTrigger:{trigger:el,start:'top 88%',once:true}}));}
 });

 /* section entrances: parts arrive in reading order, once */
 ST.batch('[data-r]',{start:'top 92%',once:true,onEnter:function(b){b.forEach(function(e){e.classList.add('in');});}});
 W.addEventListener('load',function(){ST.refresh();});

 /* count-ups (React Bits "CountUp") */
 $('[data-count]').forEach(function(el){
  var to=parseFloat(el.getAttribute('data-count')),dec=+(el.getAttribute('data-dec')||0),pre=el.getAttribute('data-pre')||'',o={v:0};
  el.textContent=pre+(0).toFixed(dec);
  g.to(o,{v:to,duration:1.6,ease:'power3.out',scrollTrigger:{trigger:el,start:'top 92%',once:true},onUpdate:function(){el.textContent=pre+o.v.toFixed(dec);}});
 });

 /* parallax */
 $('[data-speed]').forEach(function(el){
  var s=parseFloat(el.getAttribute('data-speed'));
  g.fromTo(el,{yPercent:s*10},{yPercent:-s*10,ease:'none',scrollTrigger:{trigger:el.parentNode,start:'top bottom',end:'bottom top',scrub:true}});
 });

 /* magnetic primary buttons (React Bits "Magnet"), pointer devices only */
 if(finePointer){
  $('.btn,.cell.a').forEach(function(b){
   var x=g.quickTo(b,'x',{duration:0.4,ease:'power3.out'}),y=g.quickTo(b,'y',{duration:0.4,ease:'power3.out'});
   b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();x((e.clientX-r.left-r.width/2)*0.22);y((e.clientY-r.top-r.height/2)*0.3);});
   b.addEventListener('pointerleave',function(){x(0);y(0);});
  });
 }

 /* looping scenes play only while on screen */
 function live(el,tl){ST.create({trigger:el,start:'top bottom',end:'bottom top',onToggle:function(s){s.isActive?tl.play():tl.pause();}});tl.pause();}

 var FX={
  signal:function(svg){
   var path=svg.querySelector('.sig-path'),mols=$('[data-mol]',svg),needle=svg.querySelector('.needle'),fill=svg.querySelector('.g-fill');
   g.set(needle,{rotation:-80,svgOrigin:'0 0'});
   g.set($('.chip',svg),{opacity:0,y:8});
   var tl=g.timeline({repeat:-1,repeatDelay:0.6,defaults:{ease:'power3.out'}});
   tl.fromTo($('.meal circle',svg),{y:-50,opacity:0},{y:0,opacity:1,duration:0.7,stagger:0.12,ease:'bounce.out'})
     .to(svg.querySelector('.c1'),{opacity:1,y:0,duration:0.4},'<0.2')
     .to($('.meal circle',svg),{y:170,opacity:0,duration:0.7,ease:'power2.in',stagger:0.08},'+=0.3')
     .fromTo(svg.querySelector('.gut .org'),{scale:1},{scale:1.05,transformOrigin:'50% 50%',duration:0.25,yoyo:true,repeat:1,ease:'sine.inOut'},'-=0.15')
     .to(svg.querySelector('.c2'),{opacity:1,y:0,duration:0.4},'<');
   if(W.MotionPathPlugin){
    mols.forEach(function(m,i){
     tl.fromTo(m,{opacity:0},{opacity:1,duration:0.2},'mol+='+(i*0.22));
     tl.to(m,{motionPath:{path:path,align:path,alignOrigin:[0.5,0.5],start:0,end:1},duration:1.5,ease:'power1.inOut'},'mol+='+(i*0.22));
     tl.to(m,{opacity:0,scale:0.6,duration:0.25},'mol+='+(i*0.22+1.35));
    });
   }else{tl.to(mols,{opacity:1,duration:0.3},'mol');}
   tl.fromTo(svg.querySelector('.glow circle'),{opacity:0,scale:0.8,transformOrigin:'50% 50%'},{opacity:0.35,scale:1,duration:0.5},'mol+=1.4')
     .to(svg.querySelector('.glow circle'),{opacity:0,duration:0.8},'>')
     .to(needle,{rotation:60,duration:1.6,ease:'elastic.out(1,0.75)'},'mol+=1.5')
     .to(fill,{strokeDashoffset:40,duration:1.4},'<')
     .to(svg.querySelector('.c3'),{opacity:1,y:0,duration:0.4},'<0.2')
     .to({},{duration:1.8})
     .to($('.chip',svg),{opacity:0,y:-6,duration:0.35,stagger:0.05})
     .to(needle,{rotation:-80,duration:0.6,ease:'power2.inOut'},'<')
     .to(fill,{strokeDashoffset:195,duration:0.6,ease:'power2.inOut'},'<');
   live(svg,tl);
  },
  rank:function(el){
   g.from($('.rc-bar i',el),{scaleX:0,duration:1.2,ease:OUT,stagger:0.1,scrollTrigger:{trigger:el,start:'top 90%',once:true}});
   g.from($('li',el),{x:-14,opacity:0,duration:0.7,ease:OUT,stagger:0.08,scrollTrigger:{trigger:el,start:'top 90%',once:true}});
  },
  intake:function(el){
   var li=$('li',el),ck=$('.ck',el),tl=g.timeline({repeat:-1,repeatDelay:1.2});
   tl.set(li,{opacity:0,y:10}).set(ck,{scale:0.4,opacity:0}).set(el.querySelector('.ph-prog i'),{scaleX:0})
     .to(li,{opacity:1,y:0,duration:0.45,ease:OUT,stagger:0.12});
   ck.forEach(function(c,i){tl.to(c,{scale:1,opacity:1,duration:0.35,ease:'back.out(2)'},'+=0.35').to(el.querySelector('.ph-prog i'),{scaleX:(i+1)/ck.length,duration:0.4,ease:'power2.out'},'<');});
   tl.fromTo(el.querySelector('.ph-btn'),{scale:1},{scale:0.95,duration:0.12,yoyo:true,repeat:1},'+=0.3').to({},{duration:1.2});
   live(el,tl);
  },
  review:function(el){
   var me=el.querySelector('.me'),ty=el.querySelector('.typing'),msg=el.querySelector('.msg'),tag=el.querySelector('.ui-tag');
   var tl=g.timeline({repeat:-1,repeatDelay:1.5});
   tl.set([me,ty,msg],{opacity:0,y:12,display:'none'}).call(function(){tag.textContent='Reviewing';})
     .set(me,{display:'block'}).to(me,{opacity:1,y:0,duration:0.45,ease:OUT})
     .set(ty,{display:'inline-flex'},'+=0.3').to(ty,{opacity:1,y:0,duration:0.35,ease:OUT})
     .to(ty,{opacity:0,duration:0.2},'+=1.6').set(ty,{display:'none'})
     .set(msg,{display:'block'}).to(msg,{opacity:1,y:0,duration:0.5,ease:OUT}).call(function(){tag.textContent='Reviewed';})
     .to({},{duration:2.2});
   live(el,tl);
  },
  ship:function(el){
   var li=$('li',el),bar=el.querySelector('.sh-line i'),tl=g.timeline({repeat:-1,repeatDelay:1.4});
   tl.set(bar,{scaleX:0}).call(function(){li.forEach(function(l){l.classList.remove('on');});});
   li.forEach(function(l,i){tl.to(bar,{scaleX:i/(li.length-1),duration:0.7,ease:'power2.inOut'}).call(function(){l.classList.add('on');}).fromTo(l.querySelector('.sd'),{scale:0.7},{scale:1,duration:0.4,ease:'back.out(3)'}).to({},{duration:0.35});});
   tl.fromTo(el.querySelector('.sh-box'),{rotate:0},{rotate:-10,duration:0.15,yoyo:true,repeat:3,ease:'sine.inOut'}).to({},{duration:1.4});
   live(el,tl);
  },
  price:function(el){
   g.from($('.pc-bar i',el),{scaleX:0,duration:1.1,ease:OUT,stagger:0.07,scrollTrigger:{trigger:el,start:'top 88%',once:true}});
  },
  rings:function(el){
   $('.ring-seg',el).forEach(function(s,i){
    var len=s.getAttribute('data-len'),C=s.getAttribute('stroke-dasharray').split(' ')[1];
    g.fromTo(s,{attr:{'stroke-dasharray':'0 '+C}},{attr:{'stroke-dasharray':len+' '+C},duration:1.1,delay:i*0.18,ease:'power3.inOut',scrollTrigger:{trigger:el,start:'top 85%',once:true}});
   });
  },
  orbit:function(el){
   var ring=el.querySelector('.ob-ring'),obs=$('.ob',el);
   var spin=g.to(ring,{rotation:360,duration:40,ease:'none',repeat:-1});
   var keep=g.to(obs,{rotation:-360,duration:40,ease:'none',repeat:-1});
   live(el,spin);live(el,keep);
   d.addEventListener('match',function(e){
    el.classList.add('dim');obs.forEach(function(o){o.classList.toggle('hit',o.getAttribute('data-name')===e.detail);});
    g.to([spin,keep],{timeScale:0.15,duration:0.8});
   });
  }
 };
 $('[data-fx]').forEach(function(el){var f=FX[el.getAttribute('data-fx')];if(f)f(el);});
 d.dispatchEvent(new Event('motion:on'));
})();
