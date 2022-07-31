export function searchFilters(input,selector) {
    document.addEventListener("keyup", e => {
        if (e.target.matches(input)) {
            if (e.key === "Escape") {
                e.target.value = "";
            }
            document.querySelectorAll(selector).forEach((el) => el.textContent.
            includes(e.target.value)
            ?el.classList.remove("filter")
            :el.classList.add("filter"));
        }
    });
}