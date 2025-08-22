describe("加總前端 E2E", () => {
  // 測試前提：請先啟動後端 API (http://localhost:8000) 與前端靜態伺服器 (http://localhost:5173)

  it("Test1_成功加總 2 + 3 = 5", () => {
    cy.visit("http://localhost:5173");
    cy.get('[data-cy="a"]').type("2");
    cy.get('[data-cy="b"]').type("3");
    cy.contains("計算").click();
    cy.contains("結果：5").should("be.visible");
  });

  it("Test2_成功加總 2.2 + 3.2 = 5.4", () => {
    cy.visit("http://localhost:5173");
    cy.get("#a").type("2.2");
    cy.get("#b").type("3.2");
    cy.contains("計算").click();
    cy.contains("結果：5.4").should("be.visible");
  });

  it("Test3_成功加總 2.2 + 3.2 = 5.4", () => {
    cy.visit("http://localhost:5173");
    cy.xpath('//*[@id="a"]').type("2.2");
    cy.xpath('//*[@id="b"]').type("3.2");
    cy.contains("計算").click();
    cy.contains("結果：5.4").should("be.visible");
  });

  it("Test4_輸入無效字元要提示錯誤", () => {
    cy.visit("http://localhost:5173");
    cy.get('[data-cy="a"]').type("abc");
    cy.get('[data-cy="b"]').type("3");
    cy.contains("計算").click();
    cy.contains("請輸入有效的數字").should("be.visible");
  });
});
