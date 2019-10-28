    /**
     * 新增10个科室.
     *
     */
var config = require('./config.json')

module.exports = {
  '新增科室测试': function (client) {
    const username = '#login-card-input-wrap > div:nth-child(1) > div > input' 
    const password = '#login-card-input-wrap > div:nth-child(2) > div > input'
    const login_button = '//*[@id="login-card"]/form/div[2]/button[2]'
    const xxgl_title = '//*[@id="app-list"]/div/div[1]/div/div/div[2]/div[2]/div/div[1]'
    const sbgl_title = '//*[@id="app-list"]/div/div[2]/div/div/div[2]/div[2]/div/div[1]'
    const dlgl_title = '//*[@id="app-list"]/div/div[3]/div/div/div[2]/div[2]/div/div[1]'
    const yhgl_title = '//*[@id="app-list"]/div/div[4]/div/div/div[2]/div[2]/div/div[1]'
    const bbgl_title = '//*[@id="app-list"]/div/div[5]/div/div/div[2]/div[2]/div/div[1]'
    const xtgl_title = '//*[@id="app-list"]/div/div[6]/div/div/div[2]/div[2]/div/div[1]'
    const ks_title = '/html/body/div[3]/div/h3/div'
    const ks = '//*[@id="module-modal"]/div/div[1]/div[1]/div/input'
    const bh = '//*[@id="module-modal"]/div/div[1]/div[2]/div/input'
    const xzks = '//*[@id="app-container"]/div/form/div[3]/button[2]'
    const ks_button =' /html/body/div[3]/div/div[2]/div/button[2]'
    const cx_button = '//*[@id="app-container"]/div/form/div[3]/button[1]'

    client.url(config.url).maximizeWindow()

    // Login.
    client.waitForElementVisible('#login-card', 2*config.sleep)
    client.frame(0)
    client.pause(2*config.sleep)
    client.setValue(username, config.username)
    client.setValue(password, config.password)
    client.useXpath().click(login_button)
    client.pause(3*config.sleep)
    // 科室列
    client.expect.element(xxgl_title).to.be.present
    client.pause(config.sleep)
    client.saveScreenshot('reports/xxgl_title.png')
    //client.useXpath().click(ks_title)
    client.expect.element(xzks).to.be.present
    client.pause(config.sleep)
    for( var i = 1;i < config.select_num;i++){
        ksstring = i.toString()
        bhstring = '000'+i.toString()
        client.useXpath().click(xzks)
        client.pause(config.sleep)
        client.setValue(ks,'zb'+ ksstring)
        client.setValue(bh,'zb'+ bhstring)
        client.pause(config.sleep)
        client.useXpath().click(ks_button)
        client.pause(config.sleep)
    }
    client.useXpath().click(cx_button)
    client.pause(2*config.sleep)
    client.saveScreenshot('reports/xzks.png')
    client.end()
  }
}
