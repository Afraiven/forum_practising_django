//question sliding
var elements = document.getElementsByClassName("list-group");
const tl = new TimelineMax();
var num = 0.2
for(var i=0; i<elements.length; i++) {
    var question = elements[i];
    num += 0.05
    tl.fromTo(question, 0.5, {x: "-100%", opacity: "0"}, {x: "0%", ease: Power2.easeInOut, opacity: "1"}, "-="+num);
}

//rainbow text
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

//messages disappearing
var message_ele = document.querySelector('.alert')
if (typeof message_ele != 'undefined') {
    setTimeout(function(){
        tl.fromTo(message_ele, 1, {opacity: "1", y: "0%"}, {opacity: "0", y: "-100%"});
    }, 2000);
    setTimeout(function(){
       message_ele.style.display = "none";
    }, 2100);
};

function slide() {
  if (document.getElementById("ranking-type").innerHTML == " Top 10 najwyżej ocenianych pytań "){
    document.getElementById("ranking-type").innerHTML = " Top 10 użytkowników "
    console.log(document.getElementById("ranking-type").innerHTML)
    RankingAppear()
  } else {
    document.getElementById("ranking-type").innerHTML = " Top 10 najwyżej ocenianych pytań "
    console.log(document.getElementById("ranking-type").innerHTML)
    RankingAppear()
  }
}

//appearing ranking-type
function RankingAppear() {
var element = document.getElementById("ranking-type");
t2 = new TimelineMax()
t2.fromTo(element, 1, {opacity: "0.1"}, {opacity: "1"});
}
RankingAppear()

///////////////////////////////////////
function slide() {
  if (document.getElementById("ranking-type2").innerHTML == " Top 10 najwyżej ocenianych pytań "){
    document.getElementById("ranking-type2").innerHTML = " Top 10 użytkowników "
    console.log(document.getElementById("ranking-type2").innerHTML)
    RankingAppear()
  } else {
    document.getElementById("ranking-type2").innerHTML = " Top 10 najwyżej ocenianych pytań "
    console.log(document.getElementById("ranking-type2").innerHTML)
    RankingAppear()
  }
}

//appearing ranking-type
function RankingAppear() {
var element = document.getElementById("ranking-type2");
t2 = new TimelineMax()
t2.fromTo(element, 1, {opacity: "0.1"}, {opacity: "1"});
}
RankingAppear()
//////////////////////////////

//ranking swapper
function RankingSwapper() {
  var x = document.getElementById("MyDIV");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function changeRanking() {
    var elements = document.getElementsByClassName("list-group");
   var num = 0.2
for(var i=0; i<elements.length; i++) {
    var question = elements[i];
    num += 0.05
    tl.fromTo(question, 0.5, {x: "-100%", opacity: "0"}, {x: "0%", ease: Power2.easeInOut, opacity: "1"}, "-="+num);
}
  var x = document.getElementById("hide");
  var xx = document.getElementById("show");
  if (x.style.display === "none") {
    x.style.display = "block";
    xx.style.display = "none";
  } else {
    x.style.display = "none";
    xx.style.display = "block";
  }
}

var xx = document.getElementById("show");
xx.style.display = "none";

