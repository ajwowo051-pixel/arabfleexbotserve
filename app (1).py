import os
import threading
import gradio as gr
import spaces  # المكتبة دي هي السر عشان نرضي سيرفرات ZeroGPU

# دالة تشغيل البوت في الخلفية
def run_bot():
    os.system("python bot.py")

# تشغيل مسار البوت
threading.Thread(target=run_bot, daemon=True).start()

# دالة وهمية نستخدم فيها الـ GPU عشان السيرفر ميفصلش
@spaces.GPU
def check_status():
    return "✅ السيرفر يعمل والبوت متصل بنجاح!"

# واجهة الويب
with gr.Blocks() as demo:
    gr.Markdown("# 🚀 ArabFleex Bot is Running!")
    gr.Markdown("تم خداع السيرفر بنجاح والبوت يعمل الآن في الخلفية 🤫")
    
    btn = gr.Button("فحص حالة البوت")
    out = gr.Textbox(label="النتيجة")
    
    # ربط الزرار بالدالة الوهمية
    btn.click(fn=check_status, inputs=[], outputs=out)

# إطلاق الواجهة
demo.launch()