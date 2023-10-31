# Update:从Telegram获取更新
import logging
from telegram import Update
# ContextTypes:上下文类型
from telegram.ext import ContextTypes

PAGE_SIZE = 1


# start命令
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''响应start命令'''

    # -1001902309203
    # context.bot.join_chat("-1001902309203")
    text = '您好 我是一群消息拷贝助手'
    logging.info(f"用户 {update.message.chat.username} 开始使用机器人了")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


# 定义回调函数来处理两个群组的消息
async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取群组中收到的消息
    message = update.message

    # 将消息转发到另一个群组
    message_latest_id = message.message_id
    print(message_latest_id)

    for message_id in range(1, message_latest_id + 1):

        print(message_id)
        try:
            await context.bot.copy_message(chat_id="-1001939724175", from_chat_id=message.chat.id, message_id=message_id)
        except Exception as e:
            pass

async def forward_message_re(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 获取群组中收到的消息
    message = update.message
    # 将消息转发到另一个群组
    message_latest_id = message.message_id
    print(message_latest_id)


    while True:
        print(message_latest_id)

        try:
            await context.bot.copy_message(chat_id="-1001939724175", from_chat_id=message.chat.id, message_id=message_latest_id)
        except Exception as e:
            break
        message_latest_id = message_latest_id + 1

# help命令
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''响应help命令'''

    text = '直接输入文本可以当作chatGPT用\n' \
           '机器人对接的gpt3.5\n\n' \
           '用户发送文件可以直接保存文件\n' \
           '(20MB以内 一个一个上传) \n' \
           '并在上传到云之后返回文件公网链接\n\n' \
           '/start 开始使用机器人\n' \
           '/help 获取使用帮助\n' \
           '/my 获取个人信息 仅个人机器人页面使用\n' \
           '/group 获取群组信息 仅群组使用\n' \
           '/get_bot 获取机器人 仅开发者使用\n' \
           '/get_file 获取文件 无参查所有 有参模糊查\n' \
           '/get_f_list 获取文件 分页模式 用法同上\n' \
           '/set 设置定时任务 跟间隔时间秒 勿动\n' \
           '/unset 取消定时任务 勿动\n' \

    logging.info(f"用户 {update.message.chat.username} 获取了帮助信息")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)

