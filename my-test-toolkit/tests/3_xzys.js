    /**
     * 新增10个医生.
     *
     */
var config = require('./config.json')


var randomName = require("chinese-random-name")
//生成从minNum到maxNum的随机数
function randomNum(minNum,maxNum){ 
    switch(arguments.length){ 
        case 1: 
            return parseInt(Math.random()*minNum+1,10); 
        break; 
        case 2: 
            return parseInt(Math.random()*(maxNum-minNum+1)+minNum,10); 
        break; 
            default: 
                return 0; 
            break; 
    } 
}

module.exports = {
  '新增医生测试': function (client) {
	const username ='#login-card-input-wrap > div:nth-child(1) > div > input'
	const password = '#login-card-input-wrap > div:nth-child(2) > div > input'
	const login_button = '//*[@id="login-card"]/form/div[2]/button[2]'
    const xxgl_title = '//*[@id="app-list"]/div/div[1]/div/div/div[2]/div[2]/div/div[1]'
    const ys_title = '//*[@id="app-list"]/div/div[1]/div[2]/div[3]/div'
    const xzys_button = '//*[@id="app-container"]/div/form/div[5]/button[2]'
    const xzys_title = '/html/body/div[3]/div/h3/div'
    const ys_no = '//*[@id="module-modal"]/div[1]/div[1]/div[1]/div/input'
    const ys_name = '//*[@id="module-modal"]/div[1]/div[2]/div[1]/div/input'
    const ys_sex_select = '//*[@id="module-modal"]/div[1]/div[1]/div[2]/div/div[3]/div[1]'
    const ys_zc_select = '//*[@id="module-modal"]/div[1]/div[2]/div[2]/div/div[3]/div[1]'
    const ys_ks_select = '//*[@id="module-modal"]/div[1]/div[1]/div[3]/div/div[3]'
    const ys_px_no = '//*[@id="module-modal"]/div[1]/div[2]/div[3]/div/input'
    const ys_save_button = '/html/body/div[3]/div/div[2]/div/button[2]'
    const ys_query_button = '//*[@id="app-container"]/div/form/div[5]/button[1]'

    const yszc_title = '//*[@id="app-list"]/div/div[1]/div[2]/div[5]/div/div/div[2]/div/div'
    const xzyszc_button = '//*[@id="app-container"]/div/form/div[3]/button[2]'
    const xzyszc_title = '/html/body/div[3]/div/h3/div'
    const xzyszc_no = '//*[@id="module-modal"]/div[1]/div/input'
    const xzyszc_name = '//*[@id="module-modal"]/div[2]/div/input'
    const xzyszc_num = '//*[@id="module-modal"]/div[3]/div/input'
    const xzyszc_save_button = '/html/body/div[3]/div/div[2]/div/button[2]'

    client.url(config.url).maximizeWindow()

    // Login.
    client.waitForElementVisible('#login-card', 2*config.sleep)
    client.frame(0)
    client.pause(2*config.sleep)
    client.setValue(username, config.username)
    client.setValue(password, config.password)
    client.useXpath().click(login_button)
    client.pause(3*config.sleep)
    // 医生列
    client.expect.element(ys_title).to.be.present
    client.pause(config.sleep)
    client.useXpath().click(yszc_title)
    client.pause(config.sleep)
    for( var i = 1;i < config.for_num/3;i++){
        yszcstring = i.toString()
        client.useXpath().click(xzyszc_button)
        client.expect.element(xzyszc_title).to.be.present
        client.pause(config.sleep)
        client.setValue(xzyszc_no,'zb'+yszcstring)
        client.setValue(xzyszc_name,randomName.generate())
        client.setValue(xzyszc_num,'10'+yszcstring)
        client.useXpath().click(xzyszc_save_button)
        client.pause(config.sleep)
    }

    client.useXpath().click(ys_title)
    client.pause(config.sleep)

    for( var i = 1;i < config.for_num;i++){
        ysstring = i.toString()
        bhstring = '000'+i.toString()
        client.useXpath().click(xzys_button)
        client.expect.element(xzys_title).to.be.present
        client.pause(config.sleep)
        client.setValue(ys_no,'zb'+ ysstring)
        client.setValue(ys_name,randomName.generate())
        client.click(ys_sex_select)
		random = randomNum(1,config.select_num/5)
        ys_sex_select_done = '/html/body/div[4]/div/div/div['+random.toString()+']/div/div/div[2]/div[1]'
        client.pause(2*config.sleep)
        client.useXpath().click(ys_sex_select_done)
        client.pause(config.sleep)
        client.click(ys_zc_select)
        ys_zc_select_done = '/html/body/div[4]/div/div/div['+random.toString()+']/div/div/div[2]/div[1]'
        client.pause(2*config.sleep)
        client.useXpath().click(ys_zc_select_done)
        client.click(ys_ks_select)
        ks_selectstring = randomNum(1,config.select_num)
        ks_select_done = '/html/body/div[4]/div/div/div[' + ks_selectstring.toString() +']/div/div/div[2]/div[1]'
        client.pause(2*config.sleep)
        client.useXpath().click(ks_select_done)
        client.pause(config.sleep)
        client.setValue(ys_px_no,bhstring)
        client.useXpath().click(ys_save_button)
        client.pause(config.sleep)
    }
    client.useXpath().click(ys_query_button)
    client.pause(2*config.sleep)
    client.saveScreenshot('reports/xzys.png')
    client.end()
  }
}
