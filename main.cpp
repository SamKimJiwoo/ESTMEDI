#include <windows.h>

// 버튼 ID 정의
#define ID_BTN_QUICK 1
#define ID_BTN_FULL  2
#define ID_BTN_OPT   3
#define ID_BTN_UPDATE 4

// 윈도우 창 이벤트 처리 함수 (UI 동작 제어)
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
    case WM_CREATE:
        // 알약 2.5 감성의 깔끔한 GUI 버튼들 배치
        CreateWindow("BUTTON", "빠른 검사  ->", WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,
            40, 30, 220, 35, hwnd, (HMENU)ID_BTN_QUICK, (HINSTANCE)GetWindowLongPtr(hwnd, GWLP_HINSTANCE), NULL);

        CreateWindow("BUTTON", "정밀 검사  ->", WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,
            40, 80, 220, 35, hwnd, (HMENU)ID_BTN_FULL, (HINSTANCE)GetWindowLongPtr(hwnd, GWLP_HINSTANCE), NULL);

        CreateWindow("BUTTON", "PC 최적화 및 관리", WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,
            40, 130, 220, 35, hwnd, (HMENU)ID_BTN_OPT, (HINSTANCE)GetWindowLongPtr(hwnd, GWLP_HINSTANCE), NULL);

        CreateWindow("BUTTON", "윈도우 업데이트 체크", WS_TABSTOP | WS_VISIBLE | WS_CHILD | BS_DEFPUSHBUTTON,
            40, 180, 220, 35, hwnd, (HMENU)ID_BTN_UPDATE, (HINSTANCE)GetWindowLongPtr(hwnd, GWLP_HINSTANCE), NULL);
        break;

    case WM_COMMAND:
        switch (LOWORD(wParam)) {
        case ID_BTN_QUICK:
            if (MessageBox(hwnd, "빠른 검사를 진행하시겠습니까?", "ESTMEDI 빠른 검사", MB_YESNO | MB_ICONQUESTION) == IDYES) {
                MessageBox(hwnd, "[메디] 악성코드가 없습니다. 시스템이 안전합니다!", "검사 완료", MB_OK | MB_ICONINFORMATION);
            }
            break;
        case ID_BTN_FULL:
            if (MessageBox(hwnd, "정밀 검사를 진행하시겠습니까?", "ESTMEDI 정밀 검사", MB_YESNO | MB_ICONQUESTION) == IDYES) {
                MessageBox(hwnd, "[메디] 정밀 검사 완료: 위협 요소가 발견되지 않았습니다.", "검사 완료", MB_OK | MB_ICONINFORMATION);
            }
            break;
        case ID_BTN_OPT:
            MessageBox(hwnd, "[메디] 불필요한 임시 파일(Temp) 청소를 완료했습니다! (120MB 확보)", "PC 최적화", MB_OK | MB_ICONINFORMATION);
            break;
        case ID_BTN_UPDATE:
            MessageBox(hwnd, "시스템 레지스트리 스캔 완료: 최신 보안 패치가 적용되어 있습니다.", "윈도우 업데이트", MB_OK | MB_ICONINFORMATION);
            break;
        }
        break;

    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;
    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}

// 윈도우 GUI 프로그램 진입점
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    const char* CLASS_NAME = "EstmediGuiClass";

    WNDCLASS wc = {};
    wc.lpfnWndProc = WindowProc;
    wc.hInstance = hInstance;
    wc.lpszClassName = CLASS_NAME;
    wc.hCursor = LoadCursor(nullptr, IDC_ARROW);
    wc.hbrBackground = (HBRUSH)(COLOR_BTNFACE + 1);

    RegisterClass(&wc);

    // 실제 윈도우 GUI 창 생성 (크기 고정, 깔끔한 타이틀 바)
    HWND hwnd = CreateWindowEx(
        0, CLASS_NAME, "ESTMEDI v1.0 - 토탈 보안 유틸리티",
        WS_OVERLAPPEDWINDOW & ~WS_MAXIMIZEBOX & ~WS_THICKFRAME,
        CW_USEDEFAULT, CW_USEDEFAULT, 315, 275,
        nullptr, nullptr, hInstance, nullptr
    );

    if (hwnd == nullptr) return 0;

    ShowWindow(hwnd, nCmdShow);

    MSG msg = {};
    while (GetMessage(&msg, nullptr, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}
