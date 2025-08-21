// 依你的環境調整：FastAPI 預設跑在 8000
const API_BASE = "http://localhost:8000";

const form = document.getElementById("sumForm");
const elA = document.getElementById("a");
const elB = document.getElementById("b");
const resultEl = document.getElementById("result");
const errorEl = document.getElementById("error");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  resultEl.textContent = "";
  errorEl.textContent = "";

  const a = elA.value;
  const b = elB.value;

  if (a === "" || b === "" || isNaN(Number(a)) || isNaN(Number(b))) {
    errorEl.textContent = "請輸入有效的數字";
    return;
  }

  try {
    const res = await fetch(`${API_BASE}/add`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ a: Number(a), b: Number(b) }),
    });

    if (!res.ok) {
      const t = await res.text();
      throw new Error(`API 錯誤 (${res.status}): ${t}`);
    }

    const data = await res.json();
    resultEl.textContent = `結果：${data.result}`;
  } catch (err) {
    errorEl.textContent = err.message;
  }
});
