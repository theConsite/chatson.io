function scrollToHowDoesItWork() {
    window.scrollTo(0, document.getElementById('howDoesItWork').offsetTop);
};
document.getElementById('scrollDown').addEventListener("click", scrollToHowDoesItWork, true);