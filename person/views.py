from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>صفحه اصلی | وبسایت من</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }

        /* هدر و نویگیشن */
        header {
            background: white;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }

        nav {
            max-width: 1200px;
            margin: 0 auto;
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: #667eea;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
            list-style: none;
        }

        .nav-links a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: #667eea;
        }

        /* محتوای اصلی */
        .container {
            max-width: 1200px;
            margin: 80px auto 0;
            padding: 2rem;
        }

        /* بخش قهرمان */
        .hero {
            background: white;
            border-radius: 20px;
            padding: 4rem 2rem;
            text-align: center;
            margin-bottom: 3rem;
            box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        }

        .hero h1 {
            font-size: 3rem;
            color: #667eea;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            color: #666;
            margin-bottom: 2rem;
        }

        .btn {
            display: inline-block;
            background: #667eea;
            color: white;
            padding: 12px 30px;
            border-radius: 25px;
            text-decoration: none;
            font-weight: bold;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        /* بخش ویژگی‌ها */
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .feature-card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            text-align: center;
            transition: transform 0.3s;
            box-shadow: 0 5px 20px rgba(0,0,0,0.1);
        }

        .feature-card:hover {
            transform: translateY(-5px);
        }

        .feature-icon {
            font-size: 3rem;
            margin-bottom: 1rem;
        }

        .feature-card h3 {
            color: #667eea;
            margin-bottom: 1rem;
        }

        /* فوتر */
        footer {
            background: #2d3748;
            color: white;
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
            border-radius: 20px 20px 0 0;
        }

        /* پاسخگو بودن */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
            
            .nav-links {
                gap: 1rem;
            }
            
            .container {
                padding: 1rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <nav>
            <div class="logo">وبسایت من</div>
            <ul class="nav-links">
                <li><a href="#">خانه</a></li>
                <li><a href="#">درباره ما</a></li>
                <li><a href="#">خدمات</a></li>
                <li><a href="#">تماس با ما</a></li>
            </ul>
        </nav>
    </header>

    <div class="container">
        <section class="hero">
            <h1>به وبسایت من خوش آمدید</h1>
            <p>اینجا بهترین خدمات و محصولات را برای شما فراهم کرده‌ایم</p>
            <a href="#" class="btn">شروع کنید</a>
        </section>

        <section class="features">
            <div class="feature-card">
                <div class="feature-icon">🚀</div>
                <h3>سرعت بالا</h3>
                <p>بهترین تجربه کاربری با سرعت بارگذاری فوق‌العاده</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🔒</div>
                <h3>امنیت کامل</h3>
                <p>اطلاعات شما با پیشرفته‌ترین روش‌ها محافظت می‌شود</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">💡</div>
                <h3>طراحی مدرن</h3>
                <p>طراحی زیبا و ریسپانسیو متناسب با همه دستگاه‌ها</p>
            </div>
        </section>

        <section class="features">
            <div class="feature-card">
                <div class="feature-icon">📱</div>
                <h3>واکنش‌گرا</h3>
                <p>نمایش عالی روی موبایل، تبلت و دسکتاپ</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🎨</div>
                <h3>رابط کاربری جذاب</h3>
                <p>طراحی زیبا و کاربرپسند برای بهترین تجربه</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>بهینه شده</h3>
                <p>سئو شده و کاملاً بهینه برای موتورهای جستجو</p>
            </div>
        </section>
    </div>

    <footer>
        <p>© ۲۰۲۴ وبسایت من. تمامی حقوق محفوظ است.</p>
        <p>طراحی شده با ❤️ برای شما</p>
    </footer>
</body>
</html>

""")

def abut(request):
    return HttpResponse("""<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>درباره ما</title>
    <style>
        body { font-family: Tahoma, sans-serif; line-height: 1.6; padding: 20px; background-color: #f4f4f4; color: #333; }
        .container { max-width: 800px; margin: auto; background: #fff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; }
        .btn { display: inline-block; padding: 10px 20px; background: #3498db; color: #fff; text-decoration: none; border-radius: 5px; margin-top: 20px; }
        .btn:hover { background: #2980b9; }
    </style>
</head>
<body>

<div class="container">
    <h1>درباره ما</h1>
    <p>سلام! خوش آمدید. ما در اینجا تلاش می‌کنیم تا بهترین خدمات را به شما ارائه دهیم. تخصص ما در [نام حوزه فعالیت شما] است و هدفمان جلب رضایت شماست.</p>
    
    <h2>چرا ما؟</h2>
    <ul>
        <li>کیفیت تضمین شده</li>
        <li>پشتیبانی ۲۴ ساعته</li>
        <li>تجربه و تخصص بالا</li>
    </ul>

    <a href="#" class="btn">تماس با ما</a>
</div>

</body>
</html>
""")
def shop(request):
    return HttpResponse("""
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>خرید آنلاین | فروشگاه مدرن</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Tahoma', 'Segoe UI', system-ui, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }

        .product-card {
            background: white;
            border-radius: 20px;
            overflow: hidden;
            max-width: 380px;
            width: 100%;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            transition: transform 0.3s ease;
        }

        .product-card:hover {
            transform: translateY(-5px);
        }

        .product-image {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 40px;
            text-align: center;
        }

        .product-image svg {
            width: 100px;
            height: 100px;
            filter: drop-shadow(0 5px 15px rgba(0,0,0,0.2));
        }

        .product-info {
            padding: 25px;
        }

        .product-title {
            font-size: 22px;
            color: #333;
            margin-bottom: 10px;
            font-weight: bold;
        }

        .product-description {
            color: #666;
            line-height: 1.5;
            margin-bottom: 20px;
            font-size: 13px;
        }

        .price-section {
            display: flex;
            justify-content: space-between;
            align-items: baseline;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 2px solid #f0f0f0;
        }

        .current-price {
            font-size: 26px;
            color: #667eea;
            font-weight: bold;
        }

        .current-price small {
            font-size: 12px;
            font-weight: normal;
        }

        .old-price {
            color: #999;
            text-decoration: line-through;
            font-size: 14px;
        }

        .discount {
            background: #ff4757;
            color: white;
            padding: 4px 10px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: bold;
        }

        .options {
            margin-bottom: 20px;
        }

        .label {
            font-size: 12px;
            color: #666;
            margin-bottom: 8px;
            font-weight: bold;
            display: block;
        }

        .color-options {
            display: flex;
            gap: 10px;
            margin-top: 5px;
        }

        .color {
            width: 35px;
            height: 35px;
            border-radius: 50%;
            cursor: pointer;
            transition: transform 0.2s;
            border: 2px solid transparent;
        }

        .color:hover {
            transform: scale(1.1);
        }

        input[type="radio"] {
            display: none;
        }

        input[type="radio"]:checked + .color {
            border-color: #667eea;
            box-shadow: 0 0 0 2px white, 0 0 0 4px #667eea;
        }

        .size-options {
            display: flex;
            gap: 10px;
            margin-top: 5px;
        }

        .size {
            width: 40px;
            height: 40px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s;
            font-weight: bold;
            background: white;
        }

        .size:hover {
            border-color: #667eea;
        }

        input[type="radio"]:checked + .size {
            background: #667eea;
            color: white;
            border-color: #667eea;
        }

        .quantity-select {
            width: 100%;
            padding: 10px;
            border: 2px solid #e0e0e0;
            border-radius: 10px;
            font-size: 14px;
            font-family: inherit;
            cursor: pointer;
            margin-top: 5px;
        }

        .buy-button {
            width: 100%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 15px;
            border-radius: 12px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            margin-top: 10px;
        }

        .buy-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
        }

        .buy-button:active {
            transform: translateY(0);
        }

        hr {
            margin: 15px 0;
            border: none;
            border-top: 1px solid #f0f0f0;
        }

        .features {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
            padding-top: 15px;
            border-top: 1px solid #f0f0f0;
        }

        .feature {
            text-align: center;
            font-size: 11px;
            color: #666;
        }

        .feature svg {
            width: 20px;
            height: 20px;
            margin-bottom: 5px;
        }
    </style>
</head>
<body>
    <div class="product-card">
        <div class="product-image">
            <svg viewBox="0 0 24 24" fill="white">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15h-2v-2h2v2zm0-4h-2V7h2v6z"/>
            </svg>
        </div>
        
        <div class="product-info">
            <h2 class="product-title">هدفون بی‌سیم حرفه‌ای</h2>
            <p class="product-description">
                صدای فوق‌العاده با کیفیت استودیویی، عمر باتری طولانی، طراحی ارگونومیک
            </p>
            
            <div class="price-section">
                <div>
                    <span class="current-price">1,299,000 <small>تومان</small></span>
                    <div class="old-price">1,890,000 تومان</div>
                </div>
                <span class="discount">۳۱٪ تخفیف</span>
            </div>

            <form action="#" method="POST">
                <div class="options">
                    <label class="label">انتخاب رنگ:</label>
                    <div class="color-options">
                        <label>
                            <input type="radio" name="color" value="مشکی" checked>
                            <div class="color" style="background: #2c3e50;"></div>
                        </label>
                        <label>
                            <input type="radio" name="color" value="سفید">
                            <div class="color" style="background: #ecf0f1;"></div>
                        </label>
                        <label>
                            <input type="radio" name="color" value="آبی">
                            <div class="color" style="background: #3498db;"></div>
                        </label>
                        <label>
                            <input type="radio" name="color" value="قرمز">
                            <div class="color" style="background: #e74c3c;"></div>
                        </label>
                    </div>
                </div>

                <div class="options">
                    <label class="label">اندازه:</label>
                    <div class="size-options">
                        <label>
                            <input type="radio" name="size" value="S" checked>
                            <div class="size">S</div>
                        </label>
                        <label>
                            <input type="radio" name="size" value="M">
                            <div class="size">M</div>
                        </label>
                        <label>
                            <input type="radio" name="size" value="L">
                            <div class="size">L</div>
                        </label>
                        <label>
                            <input type="radio" name="size" value="XL">
                            <div class="size">XL</div>
                        </label>
                    </div>
                </div>

                <div class="options">
                    <label class="label">تعداد:</label>
                    <select name="quantity" class="quantity-select">
                        <option value="1">1 عدد</option>
                        <option value="2">2 عدد</option>
                        <option value="3">3 عدد</option>
                        <option value="4">4 عدد</option>
                        <option value="5">5 عدد</option>
                    </select>
                </div>

                <hr>

                <button type="submit" class="buy-button">
                    🛒 خرید آنلاین
                </button>
            </form>

            <div class="features">
                <div class="feature">
                    <svg viewBox="0 0 24 24" fill="#667eea">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15h-2v-2h2v2zm0-4h-2V7h2v6z"/>
                    </svg>
                    <div>گارانتی ۱۸ ماهه</div>
                </div>
                <div class="feature">
                    <svg viewBox="0 0 24 24" fill="#667eea">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15h-2v-2h2v2zm0-4h-2V7h2v6z"/>
                    </svg>
                    <div>ارسال رایگان</div>
                </div>
                <div class="feature">
                    <svg viewBox="0 0 24 24" fill="#667eea">
                        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15h-2v-2h2v2zm0-4h-2V7h2v6z"/>
                    </svg>
                    <div>۷ روز ضمانت</div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
""")

