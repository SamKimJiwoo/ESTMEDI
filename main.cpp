#include <iostream>
#include <string>
#include <cstdlib>
#include <thread>
#include <chrono>

using namespace std;

// 화면 지우기 함수
void clearScreen() {
    #if defined(_WIN32)
        system("cls");
    #else
        cout << "\n\n"; // Cxxdroid/리눅스 환경 대응
    #endif
}

// 마스코트 '메디'가 드라이버를 돌리는 애니메이션 연출 함수
void mediActionAnimation(string actionName) {
    cout << "\n[메디 캐릭터] 마스코트 '메디'가 렌치와 드라이버를 들고 작업을 시작합니다...\n";
    string tools = "| / - \\";
    for (int i = 0; i < 4; i++) {
        cout << "\r > [MEDI Working] " << actionName << " 진행 중... [" << tools[i] << "]" << flush;
        this_thread::sleep_for(chrono::milliseconds(400));
    }
    cout << "\r > [MEDI Success] " << actionName << " 완료!          \n\n";
}

// [탭 3] 윈도우 업데이트 체크 및 버전 정보
void showTab3UpdateAndInfo() {
    int choice;
    do {
        clearScreen();
        cout << "==================================================\n";
        cout << " [ESTMEDI] 3. 윈도우 업데이트 & 버전 정보\n";
        cout << "==================================================\n";
        cout << " [1] 윈도우 업데이트 체크\n";
        cout << " [2] ESTMEDI 버전 정보 (Logo & Specs)\n";
        cout << " [3] 메인 홈으로 돌아가기\n";
        cout << "--------------------------------------------------\n";
        cout << " 선택하세요: ";
        cin >> choice;

        if (choice == 1) {
            cout << "\n[Windows Update] 시스템 레지스트리 및 패치 상태 스캔 중...\n";
            mediActionAnimation("윈도우 업데이트 점검");
            cout << " 결과: 모든 중요 보안 업데이트가 최신 상태로 안전합니다.\n";
            cout << "\n[계속하려면 엔터를 누르세요]";
            cin.ignore(); cin.get();
        } 
        else if (choice == 2) {
            cout << "\n==================================================\n";
            cout << " 프로그램 이름 : ESTMEDI (이스트메디)\n";
            cout << " 마스코트     : 메디 (드라이버와 방패를 든 수호자)\n";
            cout << " 지원 OS      : XP SP3, Vista SP2, Win 7 SP1,\n";
            cout << "                Win 8, 8.1, Win 10, Win 11\n";
            cout << " 디자인 컨셉  : 알약 2.5 스타일 클래식 유틸리티\n";
            cout << "==================================================\n";
            cout << "\n[계속하려면 엔터를 누르세요]";
            cin.ignore(); cin.get();
        }
    } while (choice != 3);
}

// [탭 2] PC 최적화 및 PC 관리
void showTab2OptimizationAndManagement() {
    int choice;
    do {
        clearScreen();
        cout << "==================================================\n";
        cout << " [ESTMEDI] 2. PC 최적화 및 PC 관리\n";
        cout << "==================================================\n";
        cout << " [1] PC 최적화 (불필요한 Temp 및 중복 파일 청소)\n";
        cout << " [2] PC 관리 (프로세스 및 시스템 상태 진단)\n";
        cout << " [3] 메인 홈으로 돌아가기\n";
        cout << "--------------------------------------------------\n";
        cout << " 선택하세요: ";
        cin >> choice;

        if (choice == 1) {
            cout << "\n[PC 최적화] 시스템 Temp 폴더 및 찌꺼기 파일 탐색 중...\n";
            mediActionAnimation("임시 파일 청소");
            cout << " 결과: 불필요한 임시 파일 38개 삭제 완료! (112 MB 확보)\n";
            cout << "\n[계속하려면 엔터를 누르세요]";
            cin.ignore(); cin.get();
        } 
        else if (choice == 2) {
            cout << "\n[PC 관리] 실행 중인 프로세스 및 메모리 점유율 분석...\n";
            mediActionAnimation("시스템 관리 진단");
            cout << " 결과: CPU 부하 정상, 메모리 여유 공간 충분함.\n";
            cout << "\n[계속하려면 엔터를 누르세요]";
            cin.ignore(); cin.get();
        }
    } while (choice != 3);
}

// [탭 1 - 하위 기능] 빠른 검사 / 정밀 검사 실행 시나리오
void runScanProcess(string scanType) {
    char confirm;
    cout << "\n[" << scanType << "] " << scanType << "를 진행하시겠습니까? (y/n): ";
    cin >> confirm;

    if (confirm == 'y' || confirm == 'Y') {
        mediActionAnimation(scanType);

        // 시뮬레이션을 위한 가상의 바이러스 검출 판정 (0개면 정상 종료, 숫자 바꾸면 치료 테스트 가능)
        int detectedViruses = 0; 

        if (detectedViruses == 0) {
            cout << "\n--------------------------------------------------\n";
            cout << " 악성코드가 없습니다! 프로그램을 종료합니다.\n";
            cout << "--------------------------------------------------\n";
            exit(0); // 요구사항: 악성코드가 없으면 메시지 띄우고 종료
        } else {
            cout << "\n--------------------------------------------------\n";
            cout << " [경고] 악성코드가 " << detectedViruses << "개가 발견되었습니다!\n";
            cout << "--------------------------------------------------\n";
            
            char healConfirm;
            cout << " 치료를 시작하시겠습니까? (네: y / 아니오: n): ";
            cin >> healConfirm;

            if (healConfirm == 'y' || healConfirm == 'Y') {
                mediActionAnimation("악성코드 치료 및 격리");
                cout << "\n[성공] 모든 위협 요소가 안전하게 치료되었습니다!\n";
            } else {
                cout << "\n[안내] 치료를 취소하였습니다. 메인 화면으로 돌아갑니다.\n";
            }
        }
    } else {
        cout << "\n[안내] 검사가 취소되었습니다.\n";
    }
    cout << "\n[계속하려면 엔터를 누르세요]";
    cin.ignore(); cin.get();
}

// [탭 1] 메인 홈 화면
int main() {
    int choice;

    // 프로그램 시작 시 환영 인사
    clearScreen();
    cout << "==================================================\n";
    cout << "     [ESTMEDI] 국산 토탈 보안 & 시스템 유틸리티    \n";
    cout << "     마스코트 '메디'가 시스템을 보호합니다.       \n";
    cout << "==================================================\n";
    cout << "\n[엔터 키를 누르면 ESTMEDI가 시작됩니다]";
    cin.ignore();

    do {
        clearScreen();
        cout << "==================================================\n";
        cout << "         ESTMEDI Security v1.0 (Home)             \n";
        cout << "==================================================\n";
        cout << " [PC 현재 상태] : 쾌적하고 안전함 (Risk Level: 0%)\n";
        cout << " [실시간 보호]  : 활성화됨 (Active Shield On)\n";
        cout << "--------------------------------------------------\n";
        cout << " [1] 빠른 검사  [바로가기 ->]\n";
        cout << " [2] 정밀 검사  [바로가기 ->]\n";
        cout << " [3] PC 최적화 및 관리 탭으로 이동\n";
        cout << " [4] 윈도우 업데이트 및 정보 탭으로 이동\n";
        cout << " [5] 프로그램 종료\n";
        cout << "==================================================\n";
        cout << " 메뉴를 선택하세요: ";
        
        if (!(cin >> choice)) {
            cin.clear(); cin.ignore(10000, '\n');
            continue;
        }

        switch(choice) {
            case 1:
                runScanProcess("빠른 검사");
                break;
            case 2:
                runScanProcess("정밀 검사");
                break;
            case 3:
                showTab2OptimizationAndManagement();
                break;
            case 4:
                showTab3UpdateAndInfo();
                break;
            case 5:
                cout << "\nESTMEDI를 종료합니다. 이용해주셔서 감사합니다!\n";
                return 0;
            default:
                cout << "\n[오류] 잘못된 번호입니다. 다시 선택해주세요.\n";
                cin.ignore(); cin.get();
        }
    } while (choice != 5);

    return 0;
}
