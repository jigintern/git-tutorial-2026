const button = document.createElement("button");
button.textContent = "Click me";

button.addEventListener("click", () => {
  console.log("hello world");
});

document.body.appendChild(button);
