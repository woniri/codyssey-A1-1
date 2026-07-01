# [기본 데이터] 이전 미션에서 작성한 프롬프트 최소 3개 등록
prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 배경을 제거하고 4K 화질로 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 글로벌 기업의 수석 IT 컨설턴트입니다. 기술적 아키텍처에 대해 초보자도 이해하기 쉽게 설명해주세요.",
        "category": "페르소나",
        "favorite": False
    }
]

def show_menu():
    """메뉴 화면을 출력하는 함수"""
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

# ... (상단의 prompts 데이터와 show_menu 함수는 그대로 둡니다) ...

def add_prompt():
    """1. 새 프롬프트를 입력받아 리스트에 추가하는 함수"""
    print("\n=== 프롬프트 추가 ===")
    
    # 1. 제목 입력 (빈 값 체크)
    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("[오류] 제목은 비어둘 수 없습니다. 다시 입력해주세요.")
        
    # 2. 내용 입력 (빈 값 체크)
    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("[오류] 내용은 비어둘 수 없습니다. 다시 입력해주세요.")

    # 3. 카테고리 선택
    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
    print("\n카테고리 선택:")
    for i, cat in enumerate(categories, 1):
        print(f"{i}) {cat}")
        
    while True:
        cat_choice = input("선택: ").strip()
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            category = categories[int(cat_choice) - 1]
            break
        print("[오류] 올바른 번호를 선택해주세요.")

    # 4. 데이터 딕셔너리 생성 후 prompts 리스트에 추가 (즐겨찾기 기본값은 False)
    new_item = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }
    prompts.append(new_item)
    print("\n프롬프트가 추가되었습니다!")

def main():
    """프로그램의 메인 루프를 담당하는 함수"""
    while True:
        show_menu()
        choice = input("선택: ").strip()
        
        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            # 임시 안내 문구를 지우고, 방금 만든 함수를 연결합니다!
            add_prompt()
        elif choice in ["2", "3", "4", "5", "6", "7"]:
            print(f"\n[안내] {choice}번 기능은 곧 구현될 예정입니다.")
        else:
            print("\n[오류] 잘못된 번호입니다. 다시 입력해주세요.")

def show_list():
    """2. 저장된 모든 프롬프트 목록을 출력하는 함수"""
    print("\n=== 프롬프트 목록 ===")
    
    # 등록된 프롬프트가 없을 때 예외 처리
    if not prompts:
        print("[안내] 등록된 프롬프트가 없습니다.")
        return

    # 순서대로 번호(i)를 붙여 출력 (1부터 시작)
    for i, p in enumerate(prompts, 1):
        # 즐겨찾기 상태에 따라 별표(⭐) 표시
        fav_icon = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{fav_icon}")
        
    print(f"\n총 {len(prompts)}개의 프롬프트")

def main():
    """프로그램의 메인 루프"""
    while True:
        show_menu()
        choice = input("선택: ").strip()
        
        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            add_prompt()
        elif choice == "2":
            # 임시 안내를 지우고 목록 함수를 연결합니다!
            show_list()
        elif choice in ["3", "4", "5", "6", "7"]:
            print(f"\n[안내] {choice}번 기능은 곧 구현될 예정입니다.")
        else:
            print("\n[오류] 잘못된 번호입니다. 다시 입력해주세요.")

def view_by_category():
    """3. 특정 카테고리를 선택하여 해당 프롬프트만 출력하는 함수"""
    categories = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
    print("\n=== 카테고리별 조회 ===")
    for i, cat in enumerate(categories, 1):
        print(f"{i}) {cat}")
        
    while True:
        cat_choice = input("선택: ").strip()
        if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(categories):
            selected_category = categories[int(cat_choice) - 1]
            break
        print("[오류] 올바른 번호를 선택해주세요.")

    print(f"\n[{selected_category}] 카테고리 프롬프트:")
    
    # 선택한 카테고리에 해당하는 프롬프트만 뽑아서 출력
    count = 0
    for p in prompts:
        if p["category"] == selected_category:
            count += 1
            fav_icon = " ⭐" if p["favorite"] else ""
            print(f"{count}. {p['title']}{fav_icon}")
            
    if count == 0:
        print("[안내] 해당 카테고리에 등록된 프롬프트가 없습니다.")
    else:
        print(f"\n총 {count}개의 프롬프트")

def main():
    """프로그램의 메인 루프"""
    while True:
        show_menu()
        choice = input("선택: ").strip()
        
        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            # 임시 안내를 지우고 카테고리 조회 함수를 연결합니다!
            view_by_category()
        elif choice in ["4", "5", "6", "7"]:
            print(f"\n[안내] {choice}번 기능은 곧 구현될 예정입니다.")
        else:
            print("\n[오류] 잘못된 번호입니다. 다시 입력해주세요.")

if __name__ == "__main__":
    main()