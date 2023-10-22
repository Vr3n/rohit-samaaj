window.addEventListener("load", function () {
  console.log("Dom content loaded!");

  anime({
    targets: "#hero-photo",
    translateY: [-250, 0],
    easing: "easeInOutSine",
    delay: 500,
    opacity: ["0%", "100%"],
  });

  anime({
    targets: "#hero-text",
    translateX: [100, 0],
    easing: "easeInOutSine",
    delay: 500,
    opacity: ["0%", "100%"],
  });

  anime({
    targets: "#hero-description",
    translateY: [250, 0],
    easing: "easeInOutSine",
    delay: 500,
    opacity: ["0%", "100%"],
  });

  anime({
    targets: "#hero-cta",
    translateY: [150, 0],
    easing: "easeInOutSine",
    delay: 500,
    opacity: ["0%", "100%"],
  });
});