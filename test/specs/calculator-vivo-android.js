// SPECIFYING THE TEST SUITE
describe("Running calculator test using webdriverio and mocha framework", function() {

    function sleep(milliseconds) {
        var start = new Date().getTime();
        for (var i = 0; i < 1e7; i++) {
          if ((new Date().getTime() - start) > milliseconds){
            break;
          }
        }
      }

    // SPECIFYING THE TEST CASE
    it("Add two numbers", async function() {

        // getting one using accessibility id
        const one = '~1';
        await $(one).click();
        await browser.pause(3000);
        // sleep(5000);

        // getting plus using accessibility id
        const plus = '~加';
        await $(plus).click();
        await browser.pause(3000);
        // sleep(5000);

        // getting seven using accessibility id
        const seven = '~7';
        await $(seven).click();
        await browser.pause(3000);
        // sleep(5000);

        // getting equal sign using accessibility id
        const equal = '~等于';
        await $(equal).click();
        await browser.saveScreenshot('./screenshots/sum.png');
        await browser.pause(5000);
        // sleep(5000);

        console.log("test done")
    });
});