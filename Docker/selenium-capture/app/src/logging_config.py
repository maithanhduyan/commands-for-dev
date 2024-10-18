import logging
import logging.config
import os
import sys

# Tạo thư mục logs nếu chưa tồn tại
if not os.path.exists('logs'):
    os.makedirs('logs')

# Định nghĩa handler tùy chỉnh hỗ trợ UTF-8
class UTF8StreamHandler(logging.StreamHandler):
    def __init__(self, stream=None):
        if stream is None:
            stream = sys.stdout
        super().__init__(stream)
        try:
            if hasattr(self.stream, 'reconfigure'):
                self.stream.reconfigure(encoding='utf-8')
            else:
                # Đối với phiên bản Python < 3.7
                import codecs
                self.stream = codecs.getwriter('utf-8')(self.stream)
        except AttributeError:
            # Xử lý nếu stream không có thuộc tính 'reconfigure'
            pass

def setup_logging():
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,  # Đảm bảo logger mặc định không bị vô hiệu hóa
        'formatters': {
            'detailed': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'console': {
                '()': UTF8StreamHandler,  # Sử dụng handler tùy chỉnh
                'formatter': 'detailed',
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'logs/app.log',
                'formatter': 'detailed',
                'level': 'INFO',
                'encoding': 'utf-8',  # Đảm bảo file log cũng được ghi với mã hóa UTF-8
            },
        },
        'loggers': {
            '': {  # Cấu hình cho logger mặc định (root logger)
                'handlers': ['console', 'file'],
                'level': 'INFO',
            },
        }
    })

# Gọi hàm này ở bất kỳ nơi nào cần cấu hình logging
setup_logging()
