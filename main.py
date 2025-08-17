class ModeToggle:
    def __init__(self):
        self.safe_mode = True  # Começa no Safe Mode

    def toggle_mode(self):
        self.safe_mode = not self.safe_mode
        mode = "Safe Mode" if self.safe_mode else "Free Mode"
        print(f"✅ Modo alterado para: {mode}")

    def get_response(self, input_text):
        if self.safe_mode:
            return self.safe_response(input_text)
        else:
            return self.free_response(input_text)

    def safe_response(self, input_text):
        return f"[Safe Mode] Resposta segura para: {input_text}"

    def free_response(self, input_text):
        return f"[Free Mode] Resposta livre para: {input_text}"


def main():
    mode_toggle = ModeToggle()
    print("🚀 Alpha iniciado! (Digite 'toggle' para mudar de modo, 'sair' para encerrar)")

    while True:
        user_input = input(">> ")
        if user_input.lower() == 'sair':
            break
        elif user_input.lower() == 'toggle':
            mode_toggle.toggle_mode()
        else:
            print(mode_toggle.get_response(user_input))


if __name__ == "__main__":
    main()
