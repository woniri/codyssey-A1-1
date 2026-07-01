import json
import os

DB_FILE = "prompts.json"
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

INITIAL_PROMPTS = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": True,
        "views": 0
    },
    {
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 배경을 제거하고 4K 화질로 생성해주세요.",
        "category": "이미지 생성",
        "favorite": False,
        "views": 0
    },
    {
        "title": "IT 컨설턴트 페르소나",
        "content": "당신은 글로벌 기업의 수석 IT 컨설턴트입니다. 기술적 아키텍처에 대해 초보자도 이해하기 쉽게 설명해주세요.",
        "category": "페르소나",
        "favorite": False,
        "views": 0
    }
]

prompts = INITIAL_PROMPTS.copy()


def load_data_manual():
    """[보너스 1] 파일에서 데이터 불러오기"""
    global prompts
    print("\n=== 파일에서 데이터 불러오기 ===")
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            prompts = json.load(f)
        for item in prompts:
            if "views" not in item:
                item["views"] = 0
        print(f"[성공] {DB_FILE} 파일로부터 데이터를 불러왔습니다! (총 {len(prompts)}개)")
    else:
        print(f"[안내] 저장된 {DB_FILE} 파일이 존재하지 않습니다. 먼저 저장을 진행해주세요.")


def save_data_manual():
    """[보너스 1] 파일에 데이터 저장"""
    print("\n=== 파일에 데이터 저장하기 ===")
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=4)
    print(f"[성공] 현재 데이터가 {DB_FILE}에 저장되었습니다!")


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기 (조회수 증가)")
    print("6. 즐겨찾기 관리 (토글)")
    print("7. 즐겨찾기 목록")
    print("8. 프롬프트 수정/삭제 (CRUD)")
    print("9. 조회수 기준 정렬 (Top 목록)")
    print("10. 카테고리별 Markdown 내보내기")
    print("11. 💾 현재 데이터 JSON 파일로 저장하기")
    print("12. 📂 JSON 파일에서 데이터 불러오기")
    print("0. 종료")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    title = input("제목: ").strip()
    while title == "":
        title = input("제목을 입력해주세요: ").strip()

    content = input("내용: ").strip()
    while content == "":
        content = input("내용을 입력해주세요: ").strip()

    print("\n카테고리 선택:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")

    cat_choice = input("선택: ").strip()
    if cat_choice.isdigit() and 1 <= int(cat_choice) <= len(CATEGORIES):
        category = CATEGORIES[int(cat_choice) - 1]
    else:
        category = "기타"

    new_item = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
        "views": 0
    }
    prompts.append(new_item)
    print(f"'{title}' 프롬프트가 임시 추가되었습니다! (영구 저장은 11번 메뉴를 이용하세요)")


def show_list():
    print("\n=== 프롬프트 목록 ===")
    if not prompts:
        print("[안내] 등록된 프롬프트가 없습니다.")
        return
    for i, p in enumerate(prompts, 1):
        fav = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{fav} (조회수: {p['views']})")


def view_by_category():
    print("\n=== 카테고리 선택 ===")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")
    choice = input("선택: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(CATEGORIES)):
        print("[오류] 잘못된 선택입니다.")
        return
    selected = CATEGORIES[int(choice) - 1]

    filtered = [p for p in prompts if p["category"] == selected]

    print(f"\n[{selected}] 카테고리 결과:")
    if not filtered:
        print("[안내] 해당 카테고리에 프롬프트가 없습니다.")
        return

    for i, p in enumerate(filtered, 1):
        fav = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']}{fav}")

    print(f"\n총 {len(filtered)}개의 프롬프트")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input("검색어 입력: ").strip()
    if not keyword:
        print("[안내] 검색어를 입력해주세요.")
        return

    results = [p for p in prompts if keyword in p["title"] or keyword in p["content"]]

    print("\n검색 결과:")
    if not results:
        print("[안내] 검색 결과가 없습니다.")
        return

    for i, p in enumerate(results, 1):
        fav = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{fav}")

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")


def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    show_list()
    if not prompts:
        return

    idx = input("\n조회할 번호 입력: ").strip()
    if not idx.isdigit() or not (1 <= int(idx) <= len(prompts)):
        print("[오류] 잘못된 번호입니다.")
        return

    p = prompts[int(idx) - 1]
    p["views"] += 1

    print("─" * 30)
    print(f"제목: {p['title']} [{'⭐' if p['favorite'] else '❌'}]")
    print(f"카테고리: {p['category']} | 조회수: {p['views']}")
    print("─" * 30)
    print(p["content"])
    print("─" * 30)


def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    show_list()
    if not prompts:
        return

    idx = input("\n즐겨찾기 토글할 번호 입력: ").strip()
    if not idx.isdigit() or not (1 <= int(idx) <= len(prompts)):
        print("[오류] 잘못된 번호입니다.")
        return

    p = prompts[int(idx) - 1]
    p["favorite"] = not p["favorite"]
    status = "추가" if p["favorite"] else "해제"
    print(f"'{p['title']}' 프롬프트를 즐겨찾기에서 {status}했습니다! (영구 저장은 11번 메뉴)")


def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    favorites = [p for p in prompts if p["favorite"]]

    if not favorites:
        print("[안내] 즐겨찾기한 프롬프트가 없습니다.")
        return

    for i, p in enumerate(favorites, 1):
        print(f"{i}. [{p['category']}] {p['title']} ⭐")

    print(f"\n총 {len(favorites)}개의 즐겨찾기")


def manage_crud():
    print("\n=== 프롬프트 수정/삭제 ===")
    show_list()
    if not prompts:
        return

    idx = input("\n작업할 프롬프트 번호 입력 (취소는 엔터): ").strip()
    if idx == "":
        return
    if not idx.isdigit() or not (1 <= int(idx) <= len(prompts)):
        print("[오류] 잘못된 번호입니다.")
        return

    target = prompts[int(idx) - 1]
    print(f"\n선택된 프롬프트: {target['title']}")
    action = input("1) 수정  2) 삭제  선택: ").strip()

    if action == "1":
        new_title = input(f"새 제목 (기존: {target['title']}) [패스는 엔터]: ").strip()
        new_content = input(f"새 내용 (기존: {target['content']}) [패스는 엔터]: ").strip()
        if new_title:
            target["title"] = new_title
        if new_content:
            target["content"] = new_content
        print("[완료] 프롬프트가 임시 수정되었습니다. (영구 저장은 11번 메뉴)")
    elif action == "2":
        prompts.remove(target)
        print("[완료] 프롬프트가 임시 삭제되었습니다. (영구 저장은 11번 메뉴)")
    else:
        print("[오류] 잘못된 선택입니다.")


def show_top_views():
    print("\n=== 조회수 기준 Top 목록 ===")
    if not prompts:
        print("[안내] 등록된 프롬프트가 없습니다.")
        return

    sorted_prompts = sorted(prompts, key=lambda x: x["views"], reverse=True)
    for i, p in enumerate(sorted_prompts, 1):
        print(f"{i}등. [{p['category']}] {p['title']} (조회수: {p['views']})")


def export_to_markdown():
    print("\n=== Markdown 내보내기 ===")
    if not prompts:
        print("[오류] 내보낼 데이터가 없습니다.")
        return

    categorized = {}
    for p in prompts:
        cat = p["category"]
        categorized.setdefault(cat, []).append(p)

    for cat, items in categorized.items():
        filename = f"{cat.replace(' ', '_')}.md"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"# {cat} 프롬프트 모음\n\n")
            for item in items:
                fav = " (★ 즐겨찾기)" if item["favorite"] else ""
                f.write(f"## {item['title']}{fav}\n")
                f.write(f"- **조회수:** {item['views']}\n\n")
                f.write(f"### 내용\n```\n{item['content']}\n```\n\n")
                f.write("---\n\n")
    print("[완료] 카테고리별 Markdown 파일 생성이 완료되었습니다!")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1": add_prompt()
        elif choice == "2": show_list()
        elif choice == "3": view_by_category()
        elif choice == "4": search_prompt()
        elif choice == "5": show_detail()
        elif choice == "6": toggle_favorite()
        elif choice == "7": show_favorites()
        elif choice == "8": manage_crud()
        elif choice == "9": show_top_views()
        elif choice == "10": export_to_markdown()
        elif choice == "11": save_data_manual()
        elif choice == "12": load_data_manual()
        else:
            print("\n[오류] 잘못된 번호입니다.")


if __name__ == "__main__":
    main()