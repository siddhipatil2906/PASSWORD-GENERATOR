# PASSWORD-GENERATOR

A sleek desktop password generator built with Python and Tkinter. Customize your password length and character types, generate a secure password instantly, check its strength, and copy it to your clipboard — all in a dark-themed GUI.

---

## Features

- 🔢 **Custom Length** — Enter any desired password length
- 🔤 **Character Options** — Choose from Letters, Numbers, and/or Symbols
- ⚡ **Instant Generation** — Generates a random password on button click
- 💪 **Strength Meter** — Rates password as Weak, Medium, or Strong based on length
- 📋 **Copy to Clipboard** — One-click copy of the generated password
- 🎨 **Dark Theme UI** — Premium dark interface with green accents

---

## Password Strength Meter

| Password Length | Strength Rating |
|-----------------|-----------------|
| 6 or fewer      | 🔴 Weak         |
| 7 – 10          | 🟠 Medium       |
| 11 or more      | 🟢 Strong       |

---

## Character Sets

| Option              | Characters Included         |
|---------------------|-----------------------------|
| Letters (A-z)       | a–z and A–Z                 |
| Numbers (0-9)       | 0–9                         |
| Symbols (!@#$)      | `! @ # $ % & * ?`           |

> All three options are enabled by default.

---

## Requirements

- Python 3.x
- `tkinter` (included with standard Python installations)
- `random` and `string` (built-in Python modules)

> No additional packages need to be installed.

---

## Usage

```bash
python PASSWORD_notepadd.py
```

1. Enter the desired **password length** in the input box
2. Check or uncheck the character type options (Letters, Numbers, Symbols)
3. Click **Generate Password**
4. The generated password appears in yellow below the button
5. The **strength label** shows Weak / Medium / Strong
6. Click **Copy Password** to copy it to your clipboard

---

## UI Layout

```
┌──────────────────────────────┐
│  🔐 Premium Password Generator│  ← Title
├──────────────────────────────┤
│    Enter Password Length      │
│         [ 12 ]                │  ← Length input
│                               │
│  ✅ Letters (A-z)             │
│  ✅ Numbers (0-9)             │
│  ✅ Symbols (!@#$)            │
│                               │
│    [ Generate Password ]      │  ← Green button
│                               │
│      aB3#kL9!mZqW             │  ← Generated password (yellow)
│          Strong               │  ← Strength label (green)
│                               │
│      [ Copy Password ]        │  ← Dark green button
└──────────────────────────────┘
```

---

## Notes

- At least one character type must be selected before generating, otherwise the app may throw an error.
- Password strength is based purely on **length** — for real security, always use all three character types.

---

## License

This project is open source and free to use.
