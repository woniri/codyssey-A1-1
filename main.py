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

def main():
    """프로그램의 메인 루프를 담당하는 함수"""
    while True:
        show_menu()
        choice = input("선택: ").strip()
        
        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice == "1":
            print("\n[안내] 프롬프트 추가 기능은 곧 구현될 예정입니다.")
        # 아직 구현되지 않은 메뉴들은 임시 처리
        elif choice in ["2", "3", "4", "5", "6", "7"]:
            print(f"\n[안내] {choice}번 기능은 곧 구현될 예정입니다.")
        else:
            print("\n[오류] 잘못된 번호입니다. 다시 입력해주세요.")

# 프로그램 시작점
if __name__ == "__main__":
    main()