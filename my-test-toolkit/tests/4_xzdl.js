    /**
     * 新增10个队列.
     *
     */
var config = require('./config.json')

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
  '新增队列信息测试': function (client) {
	const username ='#login-card-input-wrap > div:nth-child(1) > div > input'
	const password = '#login-card-input-wrap > div:nth-child(2) > div > input'
	const login_button = '//*[@id="login-card"]/form/div[2]/button[2]'
    const dlgl_title = '//*[@id="app-list"]/div/div[3]/div[1]/div/div[2]'
    const dlxx_title = '//*[@id="app-list"]/div/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div[1]'
    const xzdl_button = '//*[@id="app-container"]/div/form/div[3]/button[2]'
    const xzdl_title ='/html/body/div[3]/div/h3/div'
    const dl_name = '//*[@id="module-modal"]/div[1]/div/input'
    const dlks_select = '//*[@id="module-modal"]/div[2]/div/div[3]/div[1]'
    const dllx_select = '//*[@id="module-modal"]/div[3]/div/div[3]/div[1]'
    const dl_save_button = '/html/body/div[3]/div/div[2]/div/button[2]'
    const dl_query_button = '//*[@id="app-container"]/div/form/div[3]/button[1]'

    client.url(config.url).maximizeWindow()

    // Login.
    client.waitForElementVisible('#login-card', 2*config.sleep)
    client.frame(0)
    client.pause(2*config.sleep)
    client.setValue(username, config.username)
    client.setValue(password, config.password)
    client.useXpath().click(login_button)
    client.pause(3*config.sleep)
    // 队列信息列
    client.useXpath().click(dlgl_title)
    client.expect.element(dlxx_title).to.be.present
    client.pause(config.sleep)
    client.useXpath().click(dlxx_title)
    client.pause(config.sleep)

    for( var i = 1;i < config.for_num;i++){
        ysstring = i.toString()
        bhstring = '000'+i.toString()
        client.useXpath().click(xzdl_button)
        client.expect.element(xzdl_title).to.be.present
        client.pause(config.sleep)
        client.setValue(dl_name,'zb_'+ ysstring)
        client.useXpath().click(dlks_select)
        client.pause(2*config.sleep)
        random = randomNum(1,config.select_num)
        dlks_select_done = '/html/body/div[4]/div/div/div['+random.toString()+']/div/div/div[2]'
        client.useXpath().click(dlks_select_done)
        client.pause(config.sleep)
        client.useXpath().click(dllx_select)
        client.pause(2*config.sleep)
        random = randomNum(1,config.select_num/2-1)
        dllx_select_done = '/html/body/div[4]/div/div/div['+random.toString()+']/div/div/div[2]'
        client.useXpath().click(dllx_select_done)
        client.pause(config.sleep)
        client.useXpath().click(dl_save_button)
        client.pause(config.sleep)
        }
    client.useXpath().click(dl_query_button)
    client.pause(2*config.sleep)
    client.saveScreenshot('reports/xzdl.png')
    client.end()
    }
}
