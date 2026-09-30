"""Textes du site en vietnamien (vi/) et en coréen (ko/), lus par build.py.

Même structure que les dictionnaires français et anglais de build.py.
Traductions à faire relire par Linh.
"""

TODO = '<mark>[à compléter]</mark>'

T = {
    "vi": {
        "nav": [("prestations.html", "Dịch vụ"), ("galerie.html", "Hình ảnh"), ("faq.html", "Hỏi đáp"), ("contact.html", "Liên hệ")],
        "lang": "Ngôn ngữ",
        "book": "Đặt lịch hẹn",
        "footer": "Trang điểm cô dâu, Paris",
        "close": "Đóng",
        "zoom": "Phóng to ảnh",
        "legal": "Thông tin pháp lý",
        "privacy": "Bảo mật",
        "prev": "Ảnh trước",
        "next": "Ảnh sau",
    },
    "ko": {
        "nav": [("prestations.html", "서비스"), ("galerie.html", "갤러리"), ("faq.html", "FAQ"), ("contact.html", "문의")],
        "lang": "언어",
        "book": "예약 문의",
        "footer": "웨딩 메이크업, 파리",
        "close": "닫기",
        "zoom": "사진 크게 보기",
        "legal": "법적 고지",
        "privacy": "개인정보 처리방침",
        "prev": "이전 사진",
        "next": "다음 사진",
    },
}

C = {}

C["vi"] = dict(
    home=("Maison de Lyn · Trang điểm cô dâu tại Paris",
          "Linh, chuyên viên trang điểm cô dâu tại Paris và vùng Île-de-France. Trang điểm thử tại nhà, ngày cưới, trang điểm cho người thân.",
          None),
    services=("Dịch vụ và bảng giá · Maison de Lyn",
              "Bảng giá trang điểm cô dâu tại Paris: gói thử và ngày cưới, người thân, dặm lại, sự kiện.",
              [("Gói cô dâu", "từ 350 €", "Một buổi trang điểm thử khoảng 1 giờ 30 phút, từ hai đến bốn tháng trước đám cưới, sau đó là trang điểm ngày cưới tại nơi bạn chuẩn bị. Đã bao gồm mi giả và bộ dặm phấn."),
               ("Chỉ trang điểm thử", "120 €", "Được trừ vào gói cô dâu nếu bạn đặt lịch."),
               ("Người thân", "70 € mỗi người", "Mẹ, phù dâu, nhân chứng, được trang điểm ngay buổi sáng hôm cưới."),
               ("Dặm lại", "60 € mỗi giờ", "Tôi ở lại đến tiệc cocktail hoặc tiệc tối, và đổi kiểu trang điểm nếu bạn muốn."),
               ("Sự kiện và chụp ảnh", "từ 90 €", "Lễ đính hôn, tiệc độc thân, buổi chụp ảnh, dạ tiệc.")],
              "Miễn phí di chuyển trong Paris; báo giá riêng cho vùng Île-de-France và các nơi khác tại Pháp. Khoản đặt cọc 30 % giúp giữ ngày; phần còn lại thanh toán vào ngày cưới. Có thể có phụ phí nếu bắt đầu trước 7 giờ sáng.",
              "Dịch vụ"),
    gallery=("Hình ảnh · Maison de Lyn", "Cô dâu và ảnh chân dung nghệ thuật do Linh trang điểm, tại Paris.", "Cô dâu", "Ảnh nghệ thuật", "Xem thêm trên Instagram"),
    faq=("Hỏi đáp · Maison de Lyn", "Câu hỏi thường gặp về trang điểm cô dâu: đặt lịch, trang điểm thử, độ bền, di chuyển.",
         [("Nên đặt lịch khi nào?", "Tốt nhất là từ sáu đến mười hai tháng trước, nhất là với ngày thứ Bảy từ tháng Năm đến tháng Chín. Nếu ngày cưới đã gần, bạn cứ hỏi nhé."),
          ("Có cần trang điểm thử không?", "Tôi khuyên bạn nên thử: đó là lúc chúng ta cùng chọn kiểu trang điểm và tôi hiểu rõ làn da của bạn."),
          ("Buổi thử diễn ra ở đâu?", "Tại nhà bạn ở Paris, hoặc ở một địa điểm chúng ta cùng thống nhất."),
          ("Lớp trang điểm có giữ được cả ngày không?", "Có. Tôi dùng sản phẩm lâu trôi, không lem khi rơi nước mắt, và để lại cho bạn một bộ dặm phấn."),
          ("Da tôi nhạy cảm.", "Bạn hãy ghi rõ trong yêu cầu: tôi sẽ điều chỉnh sản phẩm và chúng ta thử trước trong buổi trang điểm thử."),
          ("Ngày cưới có thể trang điểm cho bao nhiêu người?", "Tùy vào giờ làm lễ. Mỗi người mất khoảng 45 phút; nếu nhiều hơn năm người, tôi đi cùng một trợ lý."),
          ("Bạn có nói tiếng Việt không?", "Có, tôi nói tiếng Việt, tiếng Pháp, tiếng Anh và tiếng Hàn. Tôi có thể đồng hành cùng các cô dâu từ nước ngoài đến Paris tổ chức đám cưới."),
          ("Bạn có nhận làm ngoài Paris không?", "Có, trong vùng Île-de-France và khắp nước Pháp, theo báo giá."),
          ("Đặt lịch như thế nào?", "Hãy nhắn cho tôi qua trang Liên hệ. Ngày cưới được giữ khi tôi nhận được tiền cọc và hợp đồng đã ký.")],
         "Câu hỏi"),
    contact=("Liên hệ · Maison de Lyn", "Yêu cầu báo giá trang điểm cô dâu tại Paris: phản hồi trong vòng 48 giờ.",
             "Liên hệ", "Hãy kể cho tôi về đám cưới của bạn. Tôi sẽ trả lời trong vòng 48 giờ, kèm lịch trống và báo giá.",
             dict(nom="Họ và tên", email="Email", tel="Số điện thoại", date="Ngày cưới", lieu="Thành phố nơi chuẩn bị", nb="Số người cần trang điểm",
                  prest="Dịch vụ", opts=[("mariee", "Cô dâu"), ("proches", "Chỉ người thân"), ("evenement", "Sự kiện hoặc chụp ảnh"), ("planner", "Tôi là wedding planner")],
                  style="Phong cách mong muốn", styles=["Tôi chưa biết", "Tự nhiên", "Sang trọng", "Quyến rũ"],
                  msg="Lời nhắn", send="Gửi",
                  wip="Biểu mẫu sẽ sớm hoạt động. Trong lúc chờ, bạn hãy nhắn tin cho tôi qua Instagram.",
                  ok="Cảm ơn bạn, tôi đã nhận được yêu cầu. Tôi sẽ trả lời trong vòng 48 giờ.",
                  err="Gửi không thành công. Bạn hãy thử lại hoặc nhắn tin cho tôi qua Instagram.",
                  gdpr='Thông tin của bạn chỉ được dùng để trả lời yêu cầu. <a href="confidentialite.html">Tìm hiểu thêm</a>.'),
             "Hoặc qua Instagram"),
)
C["vi"]["reviews"] = []
C["vi"]["extra"] = dict(
    styles_h="Ba phong cách",
    styles=[("Tự nhiên", "Làn da rạng rỡ, đều màu, gần như vô hình."),
            ("Sang trọng", "Đôi mắt được nhấn nhá và đôi môi nổi bật, mà vẫn là chính bạn."),
            ("Quyến rũ", "Nhiều ánh sáng, độ tương phản và chiều sâu hơn cho buổi tối.")],
    steps_h="Quy trình",
    steps=[("Trang điểm thử", "Từ hai đến bốn tháng trước, chúng ta cùng chọn kiểu trang điểm."),
           ("Ngày cưới", "Tôi đến nơi bạn chuẩn bị, mang theo đầy đủ dụng cụ."),
           ("Sau lễ cưới", "Tùy theo gói, tôi ở lại để dặm lại hoặc đổi kiểu trang điểm.")],
)

C["ko"] = dict(
    home=("Maison de Lyn · 파리 웨딩 메이크업",
          "파리와 일드프랑스에서 활동하는 웨딩 메이크업 아티스트 Linh. 방문 리허설, 본식 메이크업, 가족·지인 메이크업.",
          None),
    services=("서비스 및 가격 · Maison de Lyn",
              "파리 웨딩 메이크업 가격: 리허설과 본식 패키지, 가족·지인, 수정 메이크업, 이벤트.",
              [("신부 패키지", "350 €부터", "결혼식 2~4개월 전 약 1시간 30분의 리허설 메이크업, 그리고 준비 장소에서의 본식 메이크업. 인조 속눈썹과 수정 키트가 포함됩니다."),
               ("리허설만", "120 €", "패키지를 예약하시면 금액에서 차감됩니다."),
               ("가족·지인", "1인 70 €", "어머님, 증인, 브라이드메이드를 결혼식 당일 아침에 메이크업해 드립니다."),
               ("수정 메이크업", "시간당 60 €", "칵테일 리셉션이나 저녁 파티까지 함께하며, 원하시면 룩 체인지도 해 드립니다."),
               ("이벤트·촬영", "90 €부터", "약혼식, 브라이덜 샤워, 화보 촬영, 파티.")],
              "파리 시내 출장비는 포함되어 있으며, 일드프랑스와 프랑스 기타 지역은 별도 견적입니다. 30 % 계약금으로 날짜가 확정되며, 잔금은 당일에 결제합니다. 오전 7시 이전에 시작하면 추가 요금이 있을 수 있습니다.",
              "서비스"),
    gallery=("갤러리 · Maison de Lyn", "파리에서 Linh이 메이크업한 신부와 에디토리얼 인물 사진.", "신부", "에디토리얼", "Instagram에서 더 보기"),
    faq=("FAQ · Maison de Lyn", "웨딩 메이크업 자주 묻는 질문: 예약, 리허설, 지속력, 출장.",
         [("언제 예약해야 하나요?", "가능하면 6~12개월 전에 예약해 주세요. 특히 5월에서 9월 사이의 토요일은 빨리 마감됩니다. 날짜가 가까워도 편하게 문의해 주세요."),
          ("리허설이 꼭 필요한가요?", "추천드립니다. 함께 메이크업을 정하고, 제가 신부님의 피부를 알아가는 시간입니다."),
          ("리허설은 어디에서 하나요?", "파리의 신부님 댁이나 함께 정한 장소에서 진행합니다."),
          ("메이크업이 하루 종일 유지되나요?", "네. 눈물에도 번지지 않는 롱웨어 제품을 사용하고, 수정 키트를 드립니다."),
          ("피부가 민감해요.", "문의하실 때 알려 주세요. 제품을 맞춰 준비하고 리허설 때 미리 테스트합니다."),
          ("당일 몇 명까지 메이크업할 수 있나요?", "예식 시간에 따라 다릅니다. 1인당 약 45분이 걸리며, 5명이 넘으면 어시스턴트와 함께 갑니다."),
          ("한국어로 상담할 수 있나요?", "네, 한국어, 프랑스어, 영어, 베트남어로 상담 가능합니다. 해외에서 파리로 결혼하러 오시는 신부님도 도와드릴 수 있습니다."),
          ("파리 외 지역도 출장 가능한가요?", "네, 일드프랑스와 프랑스 전역 모두 가능하며 별도 견적입니다."),
          ("어떻게 예약하나요?", "문의 페이지로 연락 주세요. 계약금과 서명된 계약서를 받으면 날짜가 확정됩니다.")],
         "자주 묻는 질문"),
    contact=("문의 · Maison de Lyn", "파리 웨딩 메이크업 견적 문의: 48시간 이내 답변.",
             "문의", "결혼식 이야기를 들려주세요. 48시간 이내에 가능한 일정과 견적을 보내 드립니다.",
             dict(nom="이름", email="이메일", tel="전화번호", date="결혼식 날짜", lieu="준비 장소(도시)", nb="메이크업 인원",
                  prest="서비스", opts=[("mariee", "신부"), ("proches", "가족·지인만"), ("evenement", "이벤트 또는 촬영"), ("planner", "웨딩플래너입니다")],
                  style="원하는 스타일", styles=["아직 모르겠어요", "내추럴", "우아한", "글램"],
                  msg="메시지", send="보내기",
                  wip="문의 양식은 곧 열립니다. 그동안 Instagram으로 메시지를 보내 주세요.",
                  ok="감사합니다. 문의가 잘 접수되었습니다. 48시간 이내에 답변드리겠습니다.",
                  err="전송에 실패했습니다. 다시 시도하시거나 Instagram으로 메시지를 보내 주세요.",
                  gdpr='입력하신 정보는 문의에 답변하는 데에만 사용됩니다. <a href="confidentialite.html">자세히 보기</a>.'),
             "또는 Instagram으로"),
)
C["ko"]["reviews"] = []
C["ko"]["extra"] = dict(
    styles_h="세 가지 스타일",
    styles=[("내추럴", "맑고 균일한 피부, 한 듯 안 한 듯한 메이크업."),
            ("우아한", "또렷한 눈매와 존재감 있는 입술, 그러면서도 나다운 모습."),
            ("글램", "저녁을 위한 더 많은 빛과 대비, 그리고 강렬함.")],
    steps_h="진행 과정",
    steps=[("리허설", "결혼식 2~4개월 전, 함께 메이크업을 정합니다."),
           ("본식 당일", "모든 도구를 챙겨 준비 장소로 찾아갑니다."),
           ("예식 후", "패키지에 따라 수정 메이크업이나 룩 체인지를 위해 함께합니다.")],
)

H = {
    "vi": dict(h1="Trang điểm<br><em>cô dâu</em>", place="Paris và Île-de-France",
               alt_hero="Cô dâu bên cửa sổ, tay cầm bó hoa",
               marquee=["Tự nhiên", "Sang trọng", "Quyến rũ", "Thử tại nhà", "Paris", "Seoul", "Ngày cưới", "Dặm lại"],
               hello="Tôi là Linh.",
               intro="Tôi trang điểm cho cô dâu và người thân, tại nhà hoặc tại nơi bạn chuẩn bị. Một lớp trang điểm giống chính bạn, bền đẹp từ lễ cưới đến điệu nhảy cuối cùng.",
               cap1="Studio, bó hoa đỏ", cap2="Ngày cưới",
               seoul="Seoul — Paris",
               training="Được đào tạo tại Hàn Quốc, ở học viện trang điểm Art Stage 1992 tại Seoul, tôi mang đến Paris sự tỉ mỉ của trang điểm Hàn Quốc: làn da được chăm chút, rạng rỡ và tự nhiên. Tôi có thể trao đổi với bạn bằng tiếng Việt, tiếng Pháp, tiếng Anh hoặc tiếng Hàn.",
               offers=[("Gói cô dâu", "từ 350 €"), ("Người thân", "70 € mỗi người"), ("Sự kiện và chụp ảnh", "từ 90 €")],
               offers_link="Dịch vụ và bảng giá",
               closing="Hãy kể về <em>đám cưới</em> của bạn"),
    "ko": dict(h1="웨딩<br><em>메이크업</em>", place="파리 · 일드프랑스",
               alt_hero="창가에서 부케를 든 신부",
               marquee=["내추럴", "우아한", "글램", "방문 리허설", "파리", "서울", "본식", "수정 메이크업"],
               hello="Linh입니다.",
               intro="신부님과 가족분들의 메이크업을 댁이나 준비 장소에서 해 드립니다. 나다운 메이크업, 예식부터 마지막 춤까지 유지되도록.",
               cap1="스튜디오, 붉은 부케", cap2="본식 당일",
               seoul="서울 — 파리",
               training="서울의 아트스테이지1992(Art Stage 1992) 메이크업 아카데미에서 교육을 받았고, 한국 메이크업의 섬세함을 파리로 가져옵니다. 정성껏 표현한, 맑고 자연스러운 피부. 한국어, 프랑스어, 영어, 베트남어로 상담해 드립니다.",
               offers=[("신부 패키지", "350 €부터"), ("가족·지인", "1인 70 €"), ("이벤트·촬영", "90 €부터")],
               offers_link="서비스 및 가격",
               closing="<em>결혼식</em> 이야기를 들려주세요"),
}

LEGAL = {
    "vi": dict(
        legal_t="Thông tin pháp lý · Maison de Lyn", legal_h="Thông tin pháp lý",
        legal_body=f"""      <p>Bản dịch mang tính tham khảo; chỉ bản tiếng Pháp có giá trị pháp lý.</p>
      <h2>Đơn vị quản lý trang web</h2>
      <p>Maison de Lyn, {TODO} (họ tên của Linh), cá nhân kinh doanh tại Pháp.<br>
      SIRET: {TODO}<br>
      Địa chỉ: {TODO}<br>
      Email: {TODO}</p>
      <h2>Lưu trữ</h2>
      <p>GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, Hoa Kỳ.</p>
      <h2>Hình ảnh và nội dung</h2>
      <p>Hình ảnh và văn bản trên trang web thuộc về Maison de Lyn và các tác giả. Nghiêm cấm sao chép khi chưa được phép.</p>""",
        privacy_t="Bảo mật · Maison de Lyn", privacy_h="Bảo mật",
        privacy_body=f"""      <p>Bản dịch mang tính tham khảo; chỉ bản tiếng Pháp có giá trị pháp lý.</p>
      <h2>Thông tin được thu thập</h2>
      <p>Biểu mẫu liên hệ thu thập họ tên, email, số điện thoại, ngày và địa điểm cưới, số người, dịch vụ và phong cách mong muốn, cùng lời nhắn của bạn.</p>
      <h2>Mục đích sử dụng</h2>
      <p>Chỉ để trả lời yêu cầu và chuẩn bị báo giá cho bạn. Thông tin không bao giờ được bán hay dùng cho quảng cáo.</p>
      <h2>Người nhận</h2>
      <p>Linh (Maison de Lyn) và dịch vụ gửi biểu mẫu Formspree, chuyển lời nhắn của bạn qua email.</p>
      <h2>Thời gian lưu trữ</h2>
      <p>Ba năm sau lần trao đổi cuối cùng, trừ khi có hợp đồng được ký.</p>
      <h2>Quyền của bạn</h2>
      <p>Bạn có thể yêu cầu xem, sửa hoặc xóa thông tin của mình bằng cách viết tới {TODO}. Bạn cũng có thể liên hệ cơ quan bảo vệ dữ liệu của Pháp, CNIL (cnil.fr).</p>
      <h2>Cookie</h2>
      <p>Trang web không dùng cookie hay công cụ theo dõi quảng cáo. Phông chữ được lưu trữ ngay trên trang web.</p>"""),
    "ko": dict(
        legal_t="법적 고지 · Maison de Lyn", legal_h="법적 고지",
        legal_body=f"""      <p>이 번역은 참고용이며, 프랑스어 원문만 법적 효력을 가집니다.</p>
      <h2>사이트 운영자</h2>
      <p>Maison de Lyn, {TODO} (Linh의 성명), 프랑스 개인사업자.<br>
      SIRET: {TODO}<br>
      주소: {TODO}<br>
      이메일: {TODO}</p>
      <h2>호스팅</h2>
      <p>GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, 미국.</p>
      <h2>사진 및 콘텐츠</h2>
      <p>이 사이트의 사진과 글은 Maison de Lyn 및 각 저작자에게 있습니다. 허락 없는 복제를 금합니다.</p>""",
        privacy_t="개인정보 처리방침 · Maison de Lyn", privacy_h="개인정보 처리방침",
        privacy_body=f"""      <p>이 번역은 참고용이며, 프랑스어 원문만 법적 효력을 가집니다.</p>
      <h2>수집하는 정보</h2>
      <p>문의 양식은 이름, 이메일, 전화번호, 결혼식 날짜와 장소, 인원, 원하는 서비스와 스타일, 메시지를 수집합니다.</p>
      <h2>이용 목적</h2>
      <p>문의 답변과 견적 준비에만 사용하며, 판매하거나 광고에 이용하지 않습니다.</p>
      <h2>수신자</h2>
      <p>Linh(Maison de Lyn)과 문의 양식 전송 서비스 Formspree(이메일로 메시지를 전달).</p>
      <h2>보관 기간</h2>
      <p>계약을 체결하지 않은 경우, 마지막 연락 후 3년간 보관합니다.</p>
      <h2>정보 주체의 권리</h2>
      <p>{TODO}(으)로 연락하여 개인정보의 열람, 정정, 삭제를 요청할 수 있습니다. 프랑스 개인정보 보호 기관 CNIL(cnil.fr)에 민원을 제기할 수도 있습니다.</p>
      <h2>쿠키</h2>
      <p>이 사이트는 쿠키나 광고 추적 도구를 사용하지 않습니다. 글꼴은 사이트에 직접 호스팅됩니다.</p>"""),
}
