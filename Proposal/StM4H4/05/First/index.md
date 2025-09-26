# 人物設計 simple

<script src="https://cdn.jsdelivr.net/npm/js-yaml@4/dist/js-yaml.min.js"></script>
<script src="https://posetmage.com/cdn/js/parser/convertYamlToHtml.js"></script>
<script src="https://posetmage.com/cdn/js/parser/EmbbedHtmlFromYaml.js"></script>

<div yml-path="./Grumm.yml" html-path="https://shinra.posetmage.com/GameDesign/Tool/character/basic.html" height="700px">
    Loading content...
</div>

<div yml-path="./Elysia.yml" html-path="https://shinra.posetmage.com/GameDesign/Tool/character/basic.html" height="700px">
    Loading content...
</div>

<div yml-path="./Skrik.yml" html-path="https://shinra.posetmage.com/GameDesign/Tool/character/basic.html" height="700px">
    Loading content...
</div>

## 心得
GPT給的角色卡，幾乎直接google翻譯就能丟stable diffusion了

## [ChatGPT詠唱過程](./chatgpt.html)

## Stable Diffusion 詠唱過程
* txt2img
* checkpoint
    * [fantasyWorld_v1.safetensors 6870d20fac](https://civitai.com/images/125986?modelVersionId=13069&prioritizedUserIds=4104&period=AllTime&sort=Most+Reactions&limit=20)
* size
  * 480x640
* sampling
  * DPM++ SDE Karras
* seed
  * 65432123456
* negative:
  * lowres, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts,signature, watermark, username, blurry, artist name,
* positive:
  * ((high quality)), sprit water ghost, able to use ice magic, translucent body, surrounded by drops of water or frost.
  * ((high quality)), forest orc male has a stout figure, wearing a cloak and backpack made of animal skin, and the backpack contains the tools needed for hunting and gathering, There are green tattoos all over his body, showing his tribal background,There is short hair on the head and two fangs unique to orcs
  * ((high quality)), Goblin,wear night vision goggles small stature, wearing dark clothes, easy to hide. Carry a short sword and a set of burglar's tools with you.green skin and large ears, all characteristic of the Goblin tribe.

