/**
 * @author Shawan Mandal
 * @description Simple demonstration of lazy loading using an Observer. 
 */

const onScrollToBottom = document.getElementById("scroll-container") // Replace this with the container Id
// On reaching the viewport of the element, the Observer will call a function as demonstrated.

const onIntersection = ([{isIntersecting, target}]) =>
  isIntersecting && (targetAnEvent("Hello world")); // Function called
const Observer = new IntersectionObserver(onIntersection, {threshold: 1})
Observer.observe(onScrollToBottom)

function targetAnEvent(param) {
  console.log(param)
}