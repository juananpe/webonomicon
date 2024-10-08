# JavaScript in the Browser

## Overview

[% figure
   id="browser-concept-map"
   src="./browser_concept_map.svg"
   alt="concept map of JavaScript in the browser"
   caption="Concept Map"
%]

<p id="terms"></p>

## Outline

-   JavaScript was created to make web pages interactive
    -   Load into page (several ways)
    -   Trigger execution (also several ways)
    -   Manipulate [Document Object Model](g:dom) (DOM)
-   [`log_on_load.html`](./log_on_load.html)
    -   Put code directly in `<script>` tag in head of page
    -   Executed as the page loads
    -   View output in console tab in browser's developer tools
    -   But this is not reliable
        -   Code may run while browser is still converting HTML to DOM (or loading other assets)
-   [`show_headings.html`](./show_headings.html) finds things in the DOM
    -   `document` refers to the content of the page
    -   `getElementsByTagName` finds nodes match a [CSS selector](g:css-selector)
-   But it doesn't show anything
    -   Code may run etc.
-   [`show_headings_onload.html`](./show_headings_onload.html) is a better approach
    -   Define a function
    -   Use the `onload` attribute of `body` to run it when the body has fully loaded
-   [`emphasize_headings.html`](./emphasize_headings.html) modifies the DOM
    -   JavaScript changes in-memory representation of page
    -   Browser decides what to re-draw and when
-   [`emphasize_multistep.html`](./emphasize_multistep.html) does the same thing by explicitly manufacturing new nodes
-   [`button_click.html`](./button_click.html) adds a button with an [event handler](g:event-handler)
    -   Browser standards define lots of different events you can listen to
    -   You provide the function, you browser calls it when something happens
-   [`emphasize_click.html`](./emphasize_click.html)
-   [`show_hide.html`](./show_hide.html) controls visibility of elements
    -   But now we have to manage state
-   [`async_fetch.html`](./async_fetch.html) introduces two new ideas
    -   Put the code in [`async_fetch.js`](./async_fetch.js)
    -   Use [`async`](g:js-async) and [`await`](g:js-await) keywords to wait for things
    -   [`server.py`](./server.py) returns [RGB](g:rgb) color components
    -   Use `style` property rather than `setAttribute` because style can have many sub-properties
