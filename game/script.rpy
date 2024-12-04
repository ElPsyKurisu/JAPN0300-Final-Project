# このファイルにはゲームのスクリプトを記述します。

# Ren'Py のスクリプトは、インデント(行頭の空白)によってブロック分けされています。
# インデントは Tab や Shift + Tab によって調整することができます。


# まず最初に、ゲームに使うキャラクター(台詞を表示するオブジェクト)を定義します。
# 一番目のパラメーターは、テキストウィンドウに表示されるキャラクターの名前です。
# color のパラメーターを追加すると、キャラクターの名前を色付けできます。
init python:
    import random

define b = Character("ベル")
define w = Character("ウェンディ")
define r = Character("ロナルド")
define n = Character("ナレーター")
default romance_bell = False
default romance_wendy = False
default romance_ronald = False
default work_tacobell = False
default work_wendys = False
default work_mcdonalds = False
default player_name = "たけし"
default player_age = 21
default underage = False

default visited_mc = False
default visited_wendy = False
default visited_bell = False

default true_ending = False

image ronald work = "ronald_work.png"
image ronald blush = "ronald_blush.png"
image ronald disappointment = "ronald_disappointment.png"
image ronald date = "ronald_date.png"

image wendy work = "wendy_norm.png"
image wendy disappointment = "wendy_disappoint.png"
image wendy far = "wendy-far.png"
image wendy close = "wendy-close.png"
image wendy closeflip = im.Flip("wendy-close.png", horizontal=True)

image bell work = "bell_work.png"
image bell mad = "bell_mad.png"
image bell blush = "bell_blush.png"
image bell date_close = "bell_date_closeup.png"
image bell date_far = "bell_date_far.png"

image shadow_figure = "shadow.png"
# label ステートメント(文)はゲームの処理をまとめてラベル付けします。
# ラベル間の移動は jump ステートメントか call ステートメントを使います。

# ゲームは start ラベルからスタートします。

label start:
    play music "dokidoki.mp3"
    $ player_name = renpy.input("お名前は？")
    $ player_name = player_name.strip()
    if (player_name == "") :
        $ player_name = "たけし"

    $ player_age = renpy.input("何歳ですか？")
    $ player_age = player_age.strip()
    if (player_age == ""): 
        $ player_age = 21
    if int(player_age) < 15:
        $ underage = True
    if int(player_age) > 116:
        jump .liar
    $ p = Character(player_name)

    #show the dorm
    scene background_dorm
    n "%(player_name)sはここに住んでいます。%(player_name)sは%(player_age)s歳です。今、%(player_name)sはお金がなくて、恋人(こいびと)もい ないんです。とても寂(さび)しい人生を送っているので、彼を助(たす)けてくれますか?"

    p "彼氏/彼女がほしいなあ。でも、お金がない私と誰(だれ)が一緒(いっしょ)にいたいの? そろそろ、仕事をさがさないと。"

    #show a blank peace of paper
    show blank_resume at Transform(xalign=0.5, yalign=0.7, zoom=0.5)
    p "履歴書(りれきしょ)をみると、何にも書いてないんです。"

    p "わあ、これはよくないなあ。たぶんファストフードみたいなレストランでしか働けない。"
    hide blank_resume
    
    #show a google search screen
    scene google_search_screen
    "グーグル" "{i}Search results: マクドナルド、ウェンディ、 タコベル{/i}"

    p "３つのせんたくがあるので、全部に申(もう)し込(こ)みます。"

    jump .job_choice


label .job_choice:
    if underage:
        jump .underage_true
    #show providence place mall
    if (visited_bell and visited_mc and visited_wendy):
        jump .after_interviews
    else:
        scene mall_front
        n "ようやく面接(めんせつ)を受(う)ける日がきました。どのレストランに行きますか。"
        menu:
            "マクドナルド" if not visited_mc:
                "マクドナルドに行きましょう。"
                jump .mcdonalds_scene_one
            "ウェンディズ" if not visited_wendy:
                "ウェンディに行きましょう。"
                jump .wendys_scene_one
            "タコベル" if not visited_bell:
                "タコベルに行きましょう。"
                jump .tacobell_scene_one

label .mcdonalds_scene_one:
    $ correctness = 0
    scene mcdonalds_front
    p "こんにちは。私は%(player_name)sと申します。レジ係 (がかり) のお仕事に興味(きょうみ)がありますので、面接(めんせつ) を受(う)けるために参(まい)りました。"

    show ronald work at Transform(xalign=0.3, yalign=1.0, zoom=1.7)
    "..." "あ、こんにちは、%(player_name)sさん。私はロナルドと申します。"
    r "この店の社長でございます。どうぞオ フィスにお入りください。さっそくインタビューをはじめましょうか。" 

    #cut to office background
    scene office
    show gold at Transform(zoom=0.3, xalign=0.6, yalign=0.5)
    "{i}マクドナルドのオフィス{/i}"

    show ronald work at Transform(xalign=0.3, yalign=1.0, zoom=1.7)
    r "それでは、自己紹介(じこしょうかい)をお願(ねが))いいたします。"

    menu:
        "正直(しょうじき)に言うと、これまで特に仕事の経験はございません。":
            $ correctness += 1
            p "正直(しょうじき)に言うと、これまで特に仕事の経験はございません。"
            p "しかし、今日から 自分の人生(じんせい)を変(か)えたいと考えております。もしここで働かさせていただけるのであれば、かならず責任(せきにん)を持って一生懸命(いっしょうけん)働くことをお約束(やくそく)いたします。"
        "ひまな時に株取引(かぶとりひき)をするのが好き。":
            p "ひまな時に株取引(かぶとりひき)をするのが好き。" 
            p "ビットコインを聞いたことある?じつ は、お金持ちだよ。ただ、もっと金がほしくてここにアプライした。"
        
    r "このポジションに興味を持った理由(りゆう)を教えていただけますか？"

    menu: 
        "じつは、マクドナルドはどのレストランよりも私が一番好きなレストランです。":
            $ correctness += 1
            p "じつは、マクドナルドはどのレストランよりも私が一番好きなレストランです。"
        "この仕事はただの踏(ふ)み台(だい)だよ。しょうらいもっと高いポジションがほしい。と ころで、あなたの給料(きゅうりょう)はいくら?":
            p "この仕事はただの踏(ふ)み台だよ。しょうらいもっと高いポジションがほしい。と ころで、あなたの給料(きゅうりょう)はいくら？"

    r "これまでレジの仕事についてどんな経験がありますか?"

    menu:
        "家では、自分で一から手作り(てづくり)のチキンナゲットを作ります。自分ではかなり上手だと思っています。":
            $ correctness += 1
            p "家では、自分で一から手作り(てづくり)のチキンナゲットを作ります。自分ではかなり上手だと思っています。"
        "えと、むかし学校の近くにあるマクドナルドで働いた。":
            p "えと、むかし学校の近くにあるマクドナルドで働いた。"
            r "そうですか。私の友だちがその店の社長です。きっと彼に会ったことがありますよね。"
            p "えと。。。"
            show ronald disappointment at Transform(xalign=0.3,yalign=1.0, zoom=1.7)
            r "やっぱり、そこで働いていませんでしたね。"
            p "いいえ、ごめん。。。"

    show ronald_work at Transform(xalign=0.3,yalign=1.0, zoom=1.7)
    r "では、週に何日働けますか?"

    menu:
        "週に五日働くことができます。":
            $ correctness += 1
            p "週に五日働くことができます。"
        "週に二日しか働けない。私のビットコインに集中(しゅうちゅう)したいから。": 
            p "週に二日しか働けない。私のビットコインに集中(しゅうちゅう)したいから。"
    
    if (correctness >= 3):
        $ work_mcdonalds = True
        $ romance_ronald = True
        r "じつは、仕事のスキルがたりていないようですが、あなたの正直(しょうじき)さに感動(かんどう)しました。チャンスをあげます。"

        r "おめでとうございます。明日からあなたはマクドナルドで働けま す。"

        hide ronald work
        show ronald blush at Transform(xalign=0.3,yalign=1.0, zoom=1.7)
        r "ところで、今週末はひまですか?"
    else:
        r "ごめんなさい、でもこの仕事はあなたにむいていない。ほかの仕事をさがしてください。そして、まじめな目標(もくひょう)を持ってください。"
    
    $visited_mc = True
    jump .job_choice
    

label .wendys_scene_one:
    scene wendys_front
    p "こんにちは、私は%(player_name)sと申します。このレストランに興味(きょうみ)があるので、今日はインタビューに 行きます。"
    
    show wendy work at Transform(xalign=0.3, yalign=1.1)
    "..." "あー、いらっしゃいませ。ウェンディはここです。{i}キュン <3{/i} 店主。{i}キュン <3{/i}"
    w "えー、ナレーターさんは私に %(player_name)sはすごくかっこいいと言いませんでした。じゃあ、どうぞよろしく。すわってください。"

    scene office
    show harlem at Transform(zoom=0.3, xalign=0.75, yalign=0.03)
    "{i}ウェンディズのオフィス{/i}"
    $ correctness = 0
    if int(player_age) < 18:
        $ wendy_age = 23
        $ too_young_for_wendy = True
    else:
        $ wendy_age = int(player_age) + random.randint(2,5)
        $ too_young_for_wendy = False

    show wendy work at Transform(xalign=0.3, yalign=1.1)
    if too_young_for_wendy:
        w "%(player_name)sは%(player_age)sですね。じつは、あたしは%(wendy_age)sです。"
    else:
        w "%(player_name)sは%(player_age)sですね～。じつは、あたしは%(wendy_age)sです。かわいい〜"
    w "じゃあ、自己紹介(じこしょうかい)をお願(ねが)いします。"

    menu:
        "はい、今はブラウン大学へまいりました。そして、私はとてもまじめな人だと思います。":
            $ correctness += 1
            p "はい、今はブラウン大学へまいりました。そして、私はとてもまじめな人だと思います。"
        "えー、お金がほしい。ここも近くから。":
            p "えー、お金がほしい。ここも近くから。"
    
    w "では、なぜこの仕事に興味を持ったのですか?"

    menu:
        "お金!":
            p "お金!"
        "新しい方々とお話ししたり、お仕事をさせていただく練習(れんしゅう)もしたいと存(ぞん)じます。":
            $ correctness += 1
            p "新しい方々とお話ししたり、お仕事をさせていただく練習(れんしゅう)もしたいと存じます。"
    
    w "この仕事に活かせる経験がありますか。"

    menu: 
        "えと、大学の時、私は物理学部(ぶつりがくぶ)の会長だったので、たくさん経験がございます。":
            $ correctness += 1
            p "えと、大学の時、私は物理学部(ぶつりがくぶ)の会長だったので、たくさん経験がございます。"
        "えと、ウェンディとタコベルが好きなので全部大丈夫だと思います。":
            p "えと、ウェンディとタコベルが好きなので全部大丈夫だと思います。"
    
    w "どの曜日や時間帯(じかんたい)に働けますか。"

    menu:
        "いつでもいいぜ。":
            p "いつでもいいぜ。"
        "えと、土曜日と日曜日は、私は常(つね)に空(す)いております。月曜日や水曜日や金曜日もつごうがいいです。":
            $ correctness += 1
            p "えと、土曜日と日曜日は、私は常(つね)に空(す)いております。月曜日や水曜日や金曜日もつごうがいいです。"
        
    if (correctness == 4):
        $ work_wendys = True
        show wendy disappointment at Transform(xalign=0.3, yalign=1.1)
        w "まじめな人ですね。"
        show wendy work at Transform(xalign=0.3, yalign=1.1)
        w "じゃあ、フライドポテトはそこ、台所(だいどころ)はあそこ、そして、レジがここです。分(わ)かりましたか。明日は朝早くから始まります。じきゅう15ドルです。"
    
    if (2 <= correctness < 4):
        w "すみませんが、たくさんの人々がここにおうぼおしました。そして、あなたはここに マッチしません。他のところを探(さが)してください。"
    
    if (correctness <= 1):
        #show wendy in a diff emotion
        #check age to make sure
        if too_young_for_wendy:
            w "すみませんが、たくさんの人々がここにおうぼおしました。そして、あなたはここに マッチしません。他のところを探(さが)してください。"
            w "大人になったら、また挑戦してみてね～"
        else:
            w "あら〜あら〜、仕事のことを忘れてください。"
            w "私は自分で二人の生活のためにお金を稼(かせ)いでいます。明日の6時に会ってくれたら、必(かなら)ずお世話(せわ)します。"
            w "電話番号(でんわばんご)は何ですか?ラインでもいいですか?"

            menu: 
                "いいえ":
                    p "いいえ"
                "ぜったいにない":
                    p "ぜったいにない"
                "何でも言う通(とお)りだよ、ベイビー。":
                    $ romance_wendy = True
                    p "何でも言う通(とお)りだよ、ベイビー。"
                "じゃあ、また明日":
                    $ romance_wendy = True
                    p "じゃあ、また明日 :)"
    
    $ visited_wendy = True
    jump .job_choice

label .tacobell_scene_one:
    "{i}タコベルのオフィス{/i}"
    scene office
    show cowboy_hat at Transform(zoom=0.2, xalign=0.3, yalign=0.53)
    p "失礼(しつれい)いたします。"

    p "こんにちは。タコベルでレジ係(がかり)に興味がありますから、今日インタビューのためにここにまいりました。"

    show bell work at Transform(xalign=0.4, yalign=0.55, anchor=(0.5, 0.5)) 
    "..." "いいですね。インタビューを始める前に、自己紹介(じこしょうかい)をしましょうか。"
    "..." "名前はベルです。"
    b "一番大好きなことはタコスだから、ここの社長になりました。"
    b "じゃあ、インタビューを始めます。あなたのことを私に教えて下(くだ)さい。"

    $ correctness = 0
    menu:
        "私は%(player_name)sと申します。今、ブラウン大学で勉強しております。 私は本当に勤勉な人です。よろしくお願いいたします。": 
            $ correctness += 1
            p "私は%(player_name)sと申します。今、ブラウン大学で勉強しております。 私は本当に勤勉な人です。よろしくお願いいたします。"
            p "そして、ベルさんは「大好きなものはタコス」とおっしゃっていますね。実は、私もタコスが好きです。同じですね。"
            b "本当ですか!?これはマッチかもしれないです。"
            show bell blush at Transform(xalign=0.8, yalign=0.55, anchor=(0.5, 0.5))
            b "{i}＊恥(は)ずかしくなります＊{/i}"
            b "{i}＊コハンコハン＊{/i}"
        "私は%(player_name)sだ。今、ブラウン大学で勉強している。":
            p "私は%(player_name)sだ。今、ブラウン大学で勉強している。"
            p "そして、私はタコスも好きよ。よろしく。"
            show bell mad at Transform(xalign=0.6, yalign=0.55, anchor=(0.5, 0.5))
            b "初対面(しょうたいめん)なのにどうしてタメ口ですか？"
            b "ああ、%(player_name)sさんも私が何歳かわかりません。"
            b "このバイトを本当にしたいですか。"
    
    show bell work at Transform(xalign=0.4, yalign=0.55, anchor=(0.5, 0.5))
    b "とにかく、なにか過去(かこ)のアルバイトの経験がありますか。"
    menu:
        "はい、あります。いろいろな場所で働きました。だから、資格(しかく)があると思います。":
            p "はい、あります。いろいろな場所で働きました。だから、資格(しかく)があると思います。"
            show bell mad at Transform(xalign=0.6, yalign=0.55, anchor=(0.5, 0.5))
            b "ああ、いいですね。でも、大学生です。言ったことは本当ですか。"
        "いいえ、大学生だから、他のアルバイトの経験がありません。でも、ここに入ったら、もちろん学(まな)びたいです。":
            $ correctness += 1
            p "いいえ、大学生だから、他のアルバイトの経験がありません。でも、ここに入ったら、もちろん学(まな)びたいです。"
            b "大丈夫(だいじょうぶ)だと思います。ここで学んでもいいですよ。"
    
    show bell work at Transform(xalign=0.4, yalign=0.55, anchor=(0.5, 0.5))
    b "では、インタビューを終わります。"
    menu:
        "ベル社長、このインタービューをしてくださってありがとうございます。":
            $ correctness += 1
            p "ベル社長、このインタービューをしてくださってありがとうございます。"
        "ベルさん、このインタービューをしてくれてありがとう。いつでも連絡(れんらく)していいよ。":
            p "ベルさん、このインタービューをしてくれてありがとう。い つでも連絡(れんらく)していいよ。"
    
    if (correctness == 3):
        $ work_tacobell = True
        $ romance_bell = True
        n "%(player_name)sがアルバイトに採用(さいよう)されました。ベル社長は未来(みらい)について希望(きぼう)を持っています。"
        b "いい人ですね。私はすごくすごくすごく楽しみ。。。"
        show bell blush at Transform(xalign=0.8, yalign=0.55, anchor=(0.5, 0.5))
        b "{i}恥ずかしくなります{/i}"
        show bell work at Transform(xalign=0.4, yalign=0.55, anchor=(0.5, 0.5))
        b "えっと、つまり、 おめでとうございます。いつから来られますか。"
    if (1 <= correctness < 3):
        $ work_tacobell = True
        n "%(player_name)sがアルバイトに採用(さいよう)されました。でも、ベル社長は%(player_name)sの悪いところに気が付(つ)きます。"
        b "もっと従業員(じゅうぎょういん)が必要(ひつよ)だから、ここでアルバイトをしてもいいです。"
        show bell mad at Transform(xalign=0.6, yalign=0.55, anchor=(0.5, 0.5))
        b "でも、%(player_name)sの仕事をしっかりと見させてもらいます。"
    if (correctness == 0):
        n "%(player_name)sはタコベルのアルバイトができません。"
        b "すみませんが、タコベルはあなたに向(む)いていません。他のところを探(さが)してください。"
    
    $ visited_bell = True
    jump .job_choice

label .after_interviews:
    scene background_dorm
    if (not(work_mcdonalds or work_tacobell or work_wendys)):
        if (romance_wendy or romance_bell or romance_ronald):
            n "%(player_name)s はアルバイトができませんでした。"
            n "でも、ウェンディから興味があります。どうしますか。"
            menu: 
                "ウェンディとデイトをします。":
                    n "%(player_name)sはウェンディに会います。"
                    jump .wendy_good_ending
                "何もしません。":
                    n "$(player_name)sは何もしません。"
                    jump .bad_ending
        else:
            jump .bad_ending
    else:
        if (work_tacobell):
            n "ベルは%(player_name)sにレストランに手伝(てつだい)いに来てほしがっています。どうしますか。"
            menu:
                "手伝(てつだい)います。":
                    "タコベルにいきましょう。"
                    jump .tacobell_scene_two

                "いいえ。手伝いたくないです。":
                    "何もしません。"
                    n "タコベルのアルバイトを辞(や)めました。"
                    $ work_tacobell = False
                    #go to black screen
                    jump .mall_meeting_scene

label .bad_ending:
    scene game_over
    # show some type of game over screen
    n "アルバイトができません。そして、彼女/彼もできません。残念(ざんねん)ですね～。"
    n "{i}これで終わりです。わたしたちのゲームををしてくださってありがとうございます。{/i}"
    return

label .tacobell_scene_two:
    #show taco bell outside
    scene black
    show morning_sun at Transform(zoom=0.8)
    "{i}朝{/i}"
    scene black
    show taco_bell_full at Transform(zoom=1.1, xalign=0.5, yalign=0.5)
    "{i}タコベル{/i}"

    #show bell in taco bell
    show bell work at Transform(xalign=0.4, yalign=0.55, anchor=(0.5, 0.5)) 
    n "%(player_name)sはタコベルの中に行きます。ベル社長がいます。どうしますか。"
    $ correctness = 0

    menu:
        "ベルに「おはようございます」と言います。":
            $ correctness += 1
            p "おはようございます、ベル社長。"
            b "{i}＊びっくり＊{/i}"
            show bell work at Transform(xalign=0.1, yalign=0.55, anchor=(0.5, 0.5))
            b "あ、おはよう%(player_name)sさん!いっしょに良い1日を過(す)ごしましょう。"
        "同僚と話します。":
            #show bell mad
            show bell mad at Transform(xalign=0.6, yalign=0.55, anchor=(0.5, 0.5))
            b "{i}＊怒(おこ)っている＊{/i}"
            b "じゅんびをしなければいけないんだよ。覚(おぼ)えてください。"

    hide bell
    n "タコベルが開ける前に、何をしましょうか。"
    menu:
        "準備(じゅんび)をします":
            $ correctness += 1
            n "いいですね。"
        "何もしません":
            #show bell mad
            show bell mad at Transform(xalign=0.6, yalign=0.55, anchor=(0.5, 0.5))
            b "{i}＊怒っている＊{/i}"
            b "%(player_name)sさん、帰ってください。今日はあなたがやめ る日です。"
            jump .mall_meeting_scene
    #cut to black
    scene black
    show taco_bell_depraved at Transform(zoom=1.1, xalign=0.5, yalign=0.5)
    #cut to rush hour
    "ラッシュアワーの間に"

    show bell work at Transform(xalign=0.4, yalign=0.55, anchor=(0.5, 0.5)) 
    b "ああ、大変です!もう材料(ざいりょう)がないけど、お客様(きゃくさま)がたくさんいます。どうしよう?"
    p "もっと材料(ざいりょう)を持って来たほうがいいですか。"
    b "はい、ありがとうございます、%(player_name)sさん。"

    #show ingredient room (maybe like a freezer or something)
    scene black
    show freezer at Transform(zoom=0.7, xalign=0.5, yalign=0.5)
    n "材料を持ってくる時、他のレストランの社長に会いました。"
    $ antag_name = "他のレストランの社長"
    $ antag = Character("他のレストランの社長")
    if (work_wendys or work_mcdonalds):
        if (work_wendys and not work_mcdonalds):
            $ antag_name = "ウェンディ"
            $ antag = Character("ウェンディ")
        else: 
            if (work_mcdonalds and not work_wendys):
                $ antag_name = "ロナルド"
                $ antag = Character("ロナルド")
            else:
                $ choose = random.randint(1,2)
                if (choose == 1):
                    $ antag_name = "ウェンディ"
                    $ antag = Character("ウェンディ")
                if (choose == 2):
                    $antag_name = "ロナルド"
                    $ antag = Character("ロナルド")
    
    # if antag is wendy show wendy, if ronald show ronald, if none show black figure
    if (antag_name == "ウェンディ"):
        show wendy work
    elif (antag_name == "ロナルド"):
        show ronald work at Transform(xalign=0.3, yalign=1.0, zoom=1.7)
    else:
        show shadow_figure at Transform(xalign=0.5, yalign=2.0,zoom=5.0)

    antag "ああ、その服。あなたもベルで働いていますか。"
    antag "えっと。。。実(じつ)はわたしのレストランでラッシアワーがあるので。。。"
    antag "今の仕事をやめて、手伝ってくれませんか。"

    menu: 
        "じゃあ、私がお手伝いしましょう。":
            p "じゃあ、私がお手伝いしましょう。"
            antag "よかった、ちゃんと報酬(ほうしゅう)をわたしますよ。"
            n "そして、%(player_name)sは%(antag_name)sを手伝います。しかし%(player_name)sタコベルで働けなくなりました。"
            $ work_tacobell = False
            $ romance_bell = False
            $ true_ending = False
            jump .mall_meeting_scene

        "いいえ、いまベルをお手伝いしていますから、お力(ちから)にはなれません。":
            $ correctness += 1
            p "いいえ、いまベルをお手伝いしていますから、お力にはなれません。"
            antag "残念(ざんねん)だね、でもベルさんはきっと喜(よるこ)ぶでしょう。"
    
    # go to black
    scene black
    # go back to taco bell
    scene black
    show taco_bell_depraved at Transform(zoom=1.1, xalign=0.5, yalign=0.5)
    p "材料(ざいりょう)をもって来ました。"

    scene black
    show taco_bell_full at Transform(zoom=1.1, xalign=0.5, yalign=0.5)
    # show bell
    show bell work at Transform(xalign=0.4, yalign=0.55, anchor=(0.5, 0.5))
    b "ありがとう、たすかったよ!そして。。。"
    b "そんなに堅苦(かたくる)しくなくてもいいんですよ。どうせ、%(antag_name)sと出会(であ)ったことも聞いていました。"

    menu:
        "いいえ、大丈夫(だいじょうぶ)です。私はふつうのことをいたしました。":
            p "いいえ、大丈夫です。私はふつうのことをいたしました。"

        "いいえ、大丈夫だよ。私は普通(ふつう)のことをするだけ。":
            $ correctness += 1
            p "いいえ、大丈夫だよ。私は普通(ふつう)のことをするだけ。"
            #show bell blushing
            show bell blush at Transform(xalign=0.8, yalign=0.55, anchor=(0.5, 0.5))
            "{i}＊ベルの顔が赤くなります。そして、走ります。＊{/i}"
            hide bell 
    
    if (correctness == 4):
        $ romance_bell = True
        $ true_ending = True
        n "ベルは%(player_name)sにプロとしても、恋人にしても興味を持っていますし、これからもずっと一緒に仕事を続けたいと思っています。"
        #show bell again
        show bell blush at Transform(xalign=0.8, yalign=0.55, anchor=(0.5, 0.5))
        b "ところで、ショッピングモールの会議(かいぎ)があります。"
        b "他の場所でも働いているのは知ってるけど、 できれば私がいるところに集中してほしいです。"
    else:
        n "タコベルでの仕事は欲(ほ)しいなら続けてもいいですが、ベルはそれ以上(いじょう)の関係(かんけい)は望(のぞ)んでいません。"

    jump .mall_meeting_scene


label .mall_meeting_scene:
    scene black
    #show black
    n "一週間後。。。"

    scene black
    show food_court at Transform(zoom=1.6, xalign=0.5, yalign=0.5)
    #show da mall

    #show all the managers
    show ronald work at Transform(xalign=0, yalign=1.0, zoom=1.5)
    show wendy work at Transform(xalign=1.2, yalign=5.5)
    show bell work at Transform(xalign=-1.9, yalign=5.5)
    "{i}ショッピングモールの会議(かいぎ){/i}"
    n "社長がみんないます。" 
    n "ここで%(player_name)sはだれと働くか決(き)めます。そして、だれと付き合うか決めます。"
    n "まず、どこで働きたいですか。"
    hide ronald
    hide wendy
    hide bell
    $ workplace = ""
    if ((not(work_mcdonalds)) and (not(work_wendys)) and (not(work_tacobell))):
        n "アルバイトができませんでした。残念(ざんねん)ですね。"
    else:
        menu:
            "マクドナルド" if work_mcdonalds:
                #show mcdonalds logo
                show mccie at Transform(zoom=0.2, xalign=0.5, yalign=0.5)
                p "マクドナルドで働きたいです。"
                $ workplace = "マクドナルド"
            "ウェンディズ" if work_wendys:
                #show wendy's logo
                show wendys-logo at Transform(zoom=0.2, xalign=0.5, yalign=0.5)
                p "ウェンディズで働きたいです。"
                $ workplace = "ウェンディズ"
            "タコベル" if work_tacobell:
                #show tacobell logo
                show taco-bell-logo at Transform(zoom=0.15, xalign=0.5, yalign=0.5)
                p "タコベルで働きたいです。"
                $ workplace = "タコベル"
        n "おめでとうございます！%(workplace)sでアルバイトができました。"
    scene black
    show food_court at Transform(zoom=1.6, xalign=0.5, yalign=0.5)
    if (romance_bell):
        show bell work at Transform(xalign=-1.9, yalign=5.5)
    if (romance_wendy):
        show wendy work at Transform(xalign=1.2, yalign=5.5)
    if (romance_ronald):
        show ronald work at Transform(xalign=0, yalign=1.0, zoom=1.5)
    n "そして、だれと付き合いたいですか。"
    menu:
        "ロナルド" if romance_ronald:
            p "そして、ロナルドさん。。。"
            #show ronald
            hide bell
            hide wendy
            show ronald work at Transform(xalign=0.5, yalign=1.0, zoom=1.5)
            p "あなたのことが好きです。"
            #show him blushing
            show ronald blush at Transform(xalign=0.5, yalign=1.0, zoom=1.5)
            n "%(player_name)sとロナルドが付き合います。"
            #cut to black
            scene black
            n "そして、二週間後。。。"
            jump .ronald_good_ending
        "ウェンディ" if romance_wendy:
            p "そして、ウェンディさん。。。"
            hide bell
            hide ronald
            #show wendy
            show wendy work at Transform(xalign=0.55, yalign=5.5)
            p "あなたのことが好きです。"
            n "%(player_name)sとウェンディが付き合います。"
            #cut to black
            scene black
            n "そして、二週間後。。。"
            jump .wendy_good_ending

        "ベル" if romance_bell:
            p "そして、ベルさん。。。"
            hide ronald
            hide wendy
            #show bell
            show bell work at Transform(xalign=-1.9, yalign=5.5)
            p "あなたのことが好きです。"
            #show her blushing
            show bell blush at Transform(xalign=0.65, yalign=0.7, anchor=(0.5, 0.5))
            n "%(player_name)sとベルが付き合います。"
            #cut to black
            scene black
            n "そして、二週間後。。。"
            jump .bell_good_ending

label .ronald_good_ending:
    scene black
    n "ロナルドさんは%(player_name)sを迎(むか)えに行って、マクドナルドに行きます。。。"
    #show ronald
    scene mcdonalds_front
    show ronald work at Transform(xalign=0.5, yalign=1.0, zoom=1.7)
    p "送ってくれてありがとうございます。でも、今日は仕事がないですよ。。。"
    r "仕事をしに来たんじゃないです。じつは、私も恋人がいなくて。。。"
    #show ronald blushing
    show ronald blush at Transform(xalign=0.5, yalign=1.0, zoom=1.7)
    r "デートするために来ました。。。"
    p "あ、そうですか。"
    show ronald date at Transform(xalign=0.5, yalign=1.0, zoom=1.7)
    r "もちろん、私が払(はら)いますよ。"

    #cut to black
    scene black
    n "{i}これで終わりです。わたしたちのゲームをしてくださってありがとうございます。{/i}"
    return

label .bell_good_ending:
    scene aquarium
    show bell date_close at Transform(zoom=1.7, xalign=0.5, yalign=1.0)
    n "あなたとベルは恋人(こいびと)になり、仕事以外(しごといがい)の時間も一緒に過(す)ごし、関係(かんけい)を発展(はってん)させます。"

    
    #cut to black/game end
    scene black
    n "{i}これで終わりです。わたしたちのゲームをしてくださってありがとうございます。{/i}"
    return

label .wendy_good_ending:
    scene background_dorm
    show western-clothes at Transform(zoom=2.0, xalign=0.25, yalign=0.5)
    show japanese-clothes at Transform(zoom=1.2, xalign=0.75, yalign=0.5)
    n "どんな服を着ますか。"
    menu:
        "{i}洋服{/i}":
            "洋服を着ました。"
            #show player in western clothes
            
        "{i}日本の服{/i}":
            "日本の服を着ました。"
            #show player in japanese clothes

    scene wendys_front
    #show wendy closing up
    show wendy far at Transform(zoom=1.7, xalign=0.75, yalign=1.0)
    n "%(player_name)sはウェンディを見ます。そして、ウェンディのところまで歩きます。"

    #show wendy happy to see you
    show wendy close at Transform(xalign=0.4)
    w "あー、いい子だね。六時ですね。"
    p "あ、ウェンディさん!ふつうの格好(かっこう)をしていないのはめずらしいですね。"
    w "何、いやですか?"
    p "。。。"
    w "とにかく私の車はすぐ近くです。"
    
    n "%(player_name)sとウェンディは駐車場(ちゅうしゃじょう)に行きます。"
    #show parking lot with car in it
    scene parking-lot-cool
    show wendy closeflip at Transform(zoom=1.6, xalign=0.4, yalign=1.0)
    w "早く乗って。あたしが運転する。"

    scene black
    show wendy-final at Transform(zoom=0.8, xalign=0.5, yalign=0.5)
    n "%(player_name)sが車に乗り込むと、ウェンディといっしょに夕日に向かってドライブします・"
    #show sunset and game end

    scene black
    n "{i}これで終わりです。わたしたちのゲームををしてくださってありがとうございます。{/i}"
    return 

label .underage_true:
    scene game_over
    n "日本では、働くために15歳以上である必要があります。あなたは%(player_age)s歳です。両親に遊んでほしいって言ってみて！"
    return

label .liar:
    scene game_over
    n "噓（うそ）つきはどろぼうの始まり。あなたは%(player_age)s歳じゃない。やり直してください！"
    return