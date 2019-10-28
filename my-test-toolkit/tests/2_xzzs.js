    /**
     * 新增10个诊室.
     *
     */
var config = require('./config.json')

module.exports = {
  '新增诊室测试': function (client) {
    var config = require('./config.json')
	const username ='#login-card-input-wrap > div:nth-child(1) > div > input'
	const password = '#login-card-input-wrap > div:nth-child(2) > div > input'
	const login_button = '//*[@id="login-card"]/form/div[2]/button[2]'
    const xxgl_title = '//*[@id="app-list"]/div/div[1]/div/div/div[2]/div[2]/div/div[1]'
    const zs_title = '//*[@id="app-list"]/div/div[1]/div[2]/div[2]/div/div/div[2]'
    const xzzs = '//*[@id="app-container"]/div/form/div[5]/button[2]'
    const xzzs_title = '/html/body/div[3]/div/h3/div'
    const zs_name = '//*[@id="module-modal"]/div[1]/div/input'
    const ks_name = '//*[@id="module-modal"]/div[2]/div/div[3]'
    const ks_select = '/html/body/div[4]/div/div'
    const zs_save_button = '/html/body/div[3]/div/div[2]/div/button[2]'
    const zs_query_button = '//*[@id="app-container"]/div/form/div[5]/button[1]'

    client.url(config.url).maximizeWindow()

    // Login.
    client.waitForElementVisible('#login-card', 2*config.sleep)
    client.frame(0)
    client.pause(2*config.sleep)
    client.setValue(username, config.username)
    client.setValue(password, config.password)
    client.useXpath().click(login_button)
    client.pause(config.sleep)
    // 诊室列
    client.expect.element(zs_title).to.be.present
    client.pause(config.sleep)
    client.useXpath().click(zs_title)
    client.pause(config.sleep)
    for( var i = 1;i < 11;i++){
        j=i
        ksstring = i.toString()
        bhstring = '000'+i.toString()
        client.useXpath().click(xzzs)
        client.pause(config.sleep)
        client.setValue(zs_name,'zs_'+ ksstring)
        client.click(ks_name)
        ks_selectstring = j.toString()
        ks_select_done = ks_select + '/div[' + ks_selectstring +']/div/div/div[2]'
		client.pause(2*config.sleep)
        client.useXpath().click(ks_select_done)
        client.pause(config.sleep)
        client.useXpath().click(zs_save_button)
        client.pause(config.sleep)
    }
    client.useXpath().click(zs_query_button)
    client.pause(2*config.sleep)
    client.saveScreenshot('reports/zsxz.png')
    client.end()
  }
}
