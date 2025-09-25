# 選擇題 - 色彩，簡易篇

## Question

KK魔法學院助教和K大繪圖通常使用哪個色彩空間體系作為思考?

* (A) YUV, YCbCr
* (B) RGB, CMYK
* (C) CIELAB, XYZ
* (D) HSB, HSV, HLS


## Question

A處XX色為

![](./color_ring.webp)

* 相近色
* 互補色
* 相近色

## Question
![](./三大面五大調.webp)

哪個位置是XXXX?

<style>
  .option-container {
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
  }
  .option-title {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 5px;
  }
  .square {
    width: 50px;
    height: 50px;
    display: inline-block; /* Ensures squares are side-by-side */
    margin-right: 5px;
  }
  .clear {
    clear: both; /* Ensures each option container starts on a new line */
  }
</style>

## Question

哪些是X色系

<div id="quizContainer"></div>

<script>
  const options = {
    'A': ['#2dfcd9', '#0000FF', '#00FFFF', '#3c8bc0'],
    'B': ['#d84b21', '#d3a375', '#ff1d55', '#e91717'],
    'C': ['red', 'green', 'blue', 'yellow'],
    'D': ['white', 'black', 'gray', '#424242']
  };

  const container = document.getElementById('quizContainer');
  Object.keys(options).forEach(option => {
    const optionContainer = document.createElement('div');
    optionContainer.className = 'option-container';

    const title = document.createElement('div');
    title.className = 'option-title';
    title.textContent = '( ' + option + ') ';
    optionContainer.appendChild(title);

    options[option].forEach(color => {
      const square = document.createElement('div');
      square.className = 'square';
      square.style.backgroundColor = color;
      optionContainer.appendChild(square);
    });

    container.appendChild(optionContainer);
  });
</script>

