//
//var question = document.getElementById('question');
//
//const tl = new TimelineMax();
//console.log("CZE");
//console.log(question.innerHTML);
//
//tl.fromTo(question, 1.2, {x: "-100%"}, {x: "0%", ease: Power2.easeInOut})

var elements = document.getElementsByClassName("list-group");
const tl = new TimelineMax();
var num = 0.2
for(var i=0; i<elements.length; i++) {
    var question = elements[i];
    num += 0.05
    tl.fromTo(question, 0.5, {x: "-100%", opacity: "0"}, {x: "0%", ease: Power2.easeInOut, opacity: "1"}, "-="+num);
}

(function () {
  var angle = 0;
  var p = document.querySelector('.navbar-text');
  var text = p.textContent.split('');
  var len = text.length;
  var phaseJump = 360 / len;
  var spans;

  p.innerHTML = text.map(function (char) {
    return '<span>' + char + '</span>';
  }).join('');

  spans = p.children;

  (function wheee () {
    for (var i = 0; i < len; i++) {
      spans[i].style.color = 'hsl(' + (angle + Math.floor(i * phaseJump)) + ', 35%, 80%)';
    }
    angle++;
    requestAnimationFrame(wheee);
  })();
})();
