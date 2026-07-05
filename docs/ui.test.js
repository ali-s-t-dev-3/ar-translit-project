import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";

const html = readFileSync(new URL("./index.html", import.meta.url), "utf8");
const css = readFileSync(new URL("./styles.css", import.meta.url), "utf8");

test("page uses the same visible field labels as the Python Tkinter app", () => {
  assert.match(html, /Enter Arabic word transliterated in Latin:/);
  assert.match(html, /Output \(Arabic\):/);
  assert.match(html, /Suggestions:/);
  assert.match(html, /Predicted next word:/);
});

test("page uses a Tkinter-style single app window instead of the portfolio hero", () => {
  assert.doesNotMatch(html, /Type Latin\. Get Arabic\./);
  assert.doesNotMatch(html, /Quick examples/);
  assert.doesNotMatch(html, /View GitHub code/);
  assert.match(html, /class="tk-window"/);
  assert.match(css, /width:\s*500px/);
  assert.match(css, /height:\s*400px/);
});
