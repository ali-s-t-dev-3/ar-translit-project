import test from "node:test";
import assert from "node:assert/strict";

import {
  getPrediction,
  getTopSuggestions,
  transliterate,
  validateInput
} from "./app.js";

test("transliterate uses the same longest-match rules as the Python backend", () => {
  assert.equal(transliterate("alslam"), "َلسلَم");
  assert.equal(transliterate("shukran"), "شُكرَن");
  assert.equal(transliterate("bsm allh"), "بسم َلله");
});

test("dictionary suggestions use Arabic prefix matching and frequency ranking", () => {
  assert.deepEqual(getTopSuggestions("ال"), ["الله", "السلام", "الحمد"]);
  assert.deepEqual(getTopSuggestions("ك"), ["كتاب", "كتب", "كيف"]);
});

test("bigram prediction returns the highest-ranked next word or null", () => {
  assert.equal(getPrediction("السلام"), "عليكم");
  assert.equal(getPrediction("شكرا"), "جزيلا");
  assert.equal(getPrediction("كتاب"), null);
});

test("validateInput accepts Arabizi input and rejects empty or invalid input", () => {
  assert.equal(validateInput("salam"), null);
  assert.equal(validateInput(""), "Please enter a transliterated word.");
  assert.equal(validateInput("salam!"), "Invalid character detected.");
});
