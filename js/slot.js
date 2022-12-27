<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
<script src="js/jquery.easing.1.3.js"></script>
<script>
/*
Copyright 2016 Delta System Solutions Co.Ltd. All rights reserved.
*/
/*---------------------
 Customize Settings
-----------------------*/
// スロット画像配列
var slotImg = ['slot1.jpg','slot2.jpg','slot3.jpg','slot4.jpg','slot5.jpg'];
// 縦に並べるスロット画像の数
var slotNum = 50;
// スロット画像のスタート位置
var startPos = -30 * (slotNum - 3);
// スロット画像の停止位置
var stopPos = -150;
// 最後に真ん中（２行目）にくるスロット画像の番号
var middleNum = 7;
// 回転エフェクト配列（jQuery easing）
var slotEasing = ['swing','easeOutQuart','easeOutBack','easeOutBounce'];
// 回転秒数
var slotDuration = 5;
// 当たり目確率（1=100%、0.5=50%）
var kakuritu = 0.3;

/*---------------------
 Definitions
-----------------------*/
var atariIdx;
var easingIdx;
var hantei;
var time;
var result1 = new Array();
var result2 = new Array();
var result3 = new Array();

/*---------------------
 Functions
-----------------------*/
/* 初期処理 */
$(document).ready(function() {
  // 当たり判定
  atariHantei();
  // A枠にスロット画像を生成
  slotCreate( $("#slots_a .wrapper"), 1 );
  // B枠にスロット画像を生成
  slotCreate( $("#slots_b .wrapper"), 2 );
  // C枠にスロット画像を生成
  slotCreate( $("#slots_c .wrapper"), 3 );
});

/* 当たり判定 */
function atariHantei(){
  atariIdx = Math.floor(Math.random() * slotImg.length);
  hantei = Math.random() < kakuritu;
};

/* スロット画像生成 */
function slotCreate(obj, slotno){

  // アニメーションをストップ（アニメーション処理中の場合の対応）
  obj.stop(true, true);
  // 枠内の要素をクリア
  obj.children().remove();
  
  // 前回結果を退避
  // 1行目の画像INDEXをセーブ
  var save_result1 = result1[slotno];
  // 2行目の画像INDEXをセーブ
  var save_result2 = result2[slotno];
  // 3行目の画像INDEXをセーブ
  var save_result3 = result3[slotno];
  
  // スロット画像のタグ生成
  for (var i = 1; i <= slotNum; i++) {
    // 画像ファイルは配列からランダムに取得
    var idx = Math.floor(Math.random() * slotImg.length);
    
    // 画像ファイルの調整
    if (i == middleNum-1) {
      // 最後に1行目にくる画像
      result1[slotno] = idx;
    } else if (i == middleNum) {
      // 最後に2行目にくる画像
      if (hantei) {
        // 当たり判定の場合は当たり目のINDEXを設定
        idx = atariIdx;
      }
      result2[slotno] = idx;
    } else if (i == middleNum+1) {
      // 最後に3行目にくる画像
      result3[slotno] = idx;
    } else if (i == slotNum-2) {
      // 最初に1行目にくる画像
      if (save_result1 != undefined) {
        // 前回結果の1行目の画像INDEXを設定
        idx = save_result1;
      }
    } else if (i == slotNum-1) {
      // 最初に2行目にくる画像
      if (save_result2 != undefined) {
        // 前回結果の2行目の画像INDEXを設定
        idx = save_result2;
      }
    } else if (i == slotNum) {
      // 最初に3行目にくる画像
      if (save_result3 != undefined) {
        // 前回結果の3行目の画像INDEXを設定
        idx = save_result3;
      }
    }
    
    obj.append("<div class='slot'>"
    + "<img border='0'"
    + " src='img/" + slotImg[idx] + "'"
    + " width='40' height='26' />"
    + "</div>");
  }
  
  // スロット画像のスタート位置を設定
  obj.css({
    "margin-top" : startPos + "px"
  });
}

/* スロットスタート */
function slotStart(){
  
  // スタートボタンの無効化
  $("#startBtn").prop('disabled', true);
  
  // 開始メッセージ表示
  $("#slotMsg").html("GO !!");
  
  if ($("#slots_a .wrapper").css("margin-top") != startPos + "px"){
    // スロットが動いた後であれば、当たり判定を再度行なう
    atariHantei();
  }
  
  // スロットの回転秒数の取得
  time = slotDuration * 1000;
  // スロットの回転エフェクトをランダムに取得
  easingIdx = Math.floor(Math.random() * slotEasing.length);
  
  // A枠のスロット画像移動
  slotMove( $("#slots_a .wrapper"), 1 );
  // 少し遅れてB枠のスロット画像移動
  setTimeout( function() {
    slotMove($("#slots_b .wrapper"), 2 );
  }, 200);
  // さらに少し遅れてC枠のスロット画像移動
  setTimeout( function() {
    slotMove($("#slots_c .wrapper"), 3 );
  }, 400);
  
  // スロット停止後の処理（jQueryキューで回転秒数後に実行）
  $(this).delay(time+500).queue(function() {
    // 結果判定
    if (result2[1] == result2[2] && result2[1] == result2[3]) {
        // あたりメッセージ表示
        $("#slotMsg").html("BINGO !!!");
    } else {
        // はずれメッセージ表示
        $("#slotMsg").html("TRY AGAIN");
    }
    
    // スタートボタンの有効化
    $("#startBtn").prop('disabled', false);
    
    // キュー削除
    $(this).dequeue();
  });
}

/* スロット画像移動 */
function slotMove(obj, slotno){

  if (obj.css("margin-top") != startPos + "px"){
    // スロットが動いた後であれば、スロット画像を再作成
    slotCreate( obj, slotno );
  }
  
  // スロット画像の移動アニメーション
  obj.animate({
    "margin-top" : stopPos + "px"
  }, {
    'duration' : time,
    'easing' : slotEasing[easingIdx]
  });
};
</script>

<style>
* {
  box-sizing: border-box;
}

#slots_a,
#slots_b,
#slots_c {
  position: relative;
  float: left;
  width: 48px;
  height: 94px;
  background-color: white;
  border: 2px palegoldenrod outset;
  overflow: hidden;
}

#slots_a .wrapper,
#slots_b .wrapper,
#slots_c .wrapper {
  position: absolute;
  width: 46px;
}

#slots_a .wrapper .slot,
#slots_b .wrapper .slot,
#slots_c .wrapper .slot {
  width: 46px;
  height: 30px;
  text-align: center;
  padding-top: 2px;
}

.slotglass-top {
  position: absolute;
  z-index: 999;
  width: 46px;
  height: 15px;
  background: -moz-linear-gradient(top, rgba(20,20,20,0.3), rgba(20,20,20,0));
  background: -webkit-gradient(linear, left top, left bottom, from(rgba(20,20,20,0.3)), to(rgba(20,20,20,0)));
  background: -o-linear-gradient(top, rgba(20,20,20,0.3), rgba(20,20,20,0));
  background: linear-gradient(top, rgba(20,20,20,0.3), rgba(20,20,20,0));
}

.slotglass-bottom {
  position: absolute;
  z-index: 999;
  width: 45px;
  height: 15px;
  bottom: 0px;
  background: -moz-linear-gradient(top, rgba(20,20,20,0), rgba(20,20,20,0.3));
  background: -webkit-gradient(linear, left top, left bottom, from(rgba(20,20,20,0)), to(rgba(20,20,20,0.3)));
  background: -o-linear-gradient(top, rgba(20,20,20,0), rgba(20,20,20,0.3));
  background: linear-gradient(top, rgba(20,20,20,0), rgba(20,20,20,0.3));
}

.slotline {
  position: absolute;
  z-index: 999;
  width: 45px;
  height: 2px;
  top: 44px;
  opacity: 0.8;
  background-color: red;
}

#slotbox {
  background-color: #A1272E;
  box-shadow: 0px 0px 15px -5px rgba(0, 0, 0, 0.8);
  border-radius: 5px;
  width: 185px;
  padding: 20px;
  margin: 0 auto;
}

#slotMsg {
  background-color: black;
  color: white;
  font-weight: bold;
  font-size: 1em;
  text-align: center;
  border: 1px #C0C0C0 inset;
  border-radius: 5px;
  width: 100%;
  margin: 5px 0;
}

#startBtn {
  border-radius: 10px;
  background-color: gold;
  width: 100%;
  color: white;
  font-weight: bold;
  text-shadow:1px 1px 2px #333;
  outline: 0;
}
</style>

<div id="slotbox">

<div id="slots_a">
  <div class="wrapper"></div>
  <div class="slotglass-top"></div>
  <div class="slotglass-bottom"></div>
  <div class="slotline"></div>
</div>
<div id="slots_b">
  <div class="wrapper"></div>
  <div class="slotglass-top"></div>
  <div class="slotglass-bottom"></div>
  <div class="slotline"></div>
</div>
<div id="slots_c">
  <div class="wrapper"></div>
  <div class="slotglass-top"></div>
  <div class="slotglass-bottom"></div>
  <div class="slotline"></div>
</div>

<br style="clear: both" />

<div id="slotMsg">Let' Start<br/></div>
<input id="startBtn" type="button" value="START" onclick="javascript:slotStart();" />

</div>