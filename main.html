<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health Assistant</title>
    <link href="https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --glass-bg: rgba(255, 255, 255, 0.18);
            --glass-border: rgba(255,255,255,0.35);
            --glass-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.18);
            --glass-blur: 16px;
            --glass-radius: 24px;
            --accent-gradient: linear-gradient(135deg, #aee2ff 0%, #e0c3fc 100%);
            --apple-blue: #007aff;
            --apple-gray: #f5f6fa;
            --apple-dark: #222;
            --apple-light: #fff;
            --font-family: 'Segoe UI', 'San Francisco', 'Arial', sans-serif;
        }

        body {
            margin: 0;
            font-family: var(--font-family);
            background: var(--accent-gradient);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: var(--apple-dark);
        }

        .app-container {
            width: 100%;
            max-width: 900px;
            min-height: 90vh;
            background: var(--glass-bg);
            border-radius: var(--glass-radius);
            box-shadow: var(--glass-shadow);
            backdrop-filter: blur(var(--glass-blur));
            -webkit-backdrop-filter: blur(var(--glass-blur));
            border: 1px solid var(--glass-border);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            position: relative;
        }

        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 24px;
            height: 64px;
            background: var(--glass-bg);
            border-bottom: 1px solid var(--glass-border);
            box-shadow: 0 2px 8px rgba(31,38,135,0.08);
            z-index: 101;
            backdrop-filter: blur(8px);
        }
        .header-title {
            font-size: 1.5em;
            font-weight: 700;
            color: var(--apple-dark);
            margin: 0;
            flex-grow: 1;
            text-align: center;
            letter-spacing: 0.02em;
        }
        .header-icon-btn {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 50%;
            padding: 8px;
            cursor: pointer;
            color: var(--apple-blue);
            box-shadow: 0 2px 8px rgba(31,38,135,0.08);
            transition: background 0.2s;
        }
        .header-icon-btn:hover {
            background: rgba(255,255,255,0.28);
        }
        .header-icon-btn svg {
            width: 24px;
            height: 24px;
            fill: currentColor;
        }
        .user-avatar {
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: var(--apple-blue);
            color: var(--apple-light);
            display: flex;
            justify-content: center;
            align-items: center;
            font-weight: bold;
            font-size: 1em;
            margin-left: 10px;
            box-shadow: 0 2px 8px rgba(31,38,135,0.08);
        }

        .sidebar {
            position: fixed;
            top: 0;
            left: 0;
            width: 260px;
            height: 100%;
            background: var(--glass-bg);
            box-shadow: var(--glass-shadow);
            border-right: 1px solid var(--glass-border);
            transform: translateX(-100%);
            transition: transform 0.3s ease-in-out;
            z-index: 102;
            padding-top: 64px;
            backdrop-filter: blur(var(--glass-blur));
            display: flex;
            flex-direction: column;
            overflow-y: auto;
        }
        .sidebar.open {
            transform: translateX(0);
        }
        .sidebar-menu {
            list-style: none;
            padding: 0;
            margin: 0;
            flex-grow: 1;
        }
        .sidebar-menu-item {
            display: flex;
            align-items: center;
            padding: 16px 24px;
            cursor: pointer;
            color: var(--apple-dark);
            text-decoration: none;
            transition: background 0.2s;
            font-size: 1em;
            font-weight: 500;
            border-radius: 12px;
        }
        .sidebar-menu-item:hover, .sidebar-menu-item.active {
            background: rgba(255,255,255,0.28);
            color: var(--apple-blue);
        }
        .sidebar-menu-item svg {
            width: 22px;
            height: 22px;
            margin-right: 15px;
            fill: var(--apple-blue);
        }
        .sidebar-divider {
            border-top: 1px solid var(--glass-border);
            margin: 10px 24px;
        }
        .sidebar-features-title {
            font-size: 0.95em;
            color: var(--apple-blue);
            padding: 10px 24px 5px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-weight: 600;
        }
        .sidebar-feature-list {
            list-style: none;
            padding: 0 24px;
            margin: 0;
        }
        .sidebar-feature-list-item {
            display: flex;
            align-items: flex-start;
            margin-bottom: 10px;
            font-size: 0.9em;
            color: var(--apple-dark);
        }
        .sidebar-feature-list-item::before {
            content: '•';
            color: var(--apple-blue);
            font-size: 1.2em;
            line-height: 1;
            margin-right: 8px;
        }

        .overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(31,38,135,0.18);
            z-index: 100;
            opacity: 0;
            visibility: hidden;
            transition: opacity 0.3s;
            backdrop-filter: blur(4px);
        }
        .overlay.active {
            opacity: 1;
            visibility: visible;
        }

        .main-content-area {
            flex-grow: 1;
            overflow-y: auto;
            padding: 32px 0;
            box-sizing: border-box;
            background: transparent;
        }
        .welcome-section, .chat-section {
            padding-left: 32px;
            padding-right: 32px;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
            box-sizing: border-box;
        }

        .welcome-section {
            text-align: center;
            background: var(--glass-bg);
            border-radius: var(--glass-radius);
            box-shadow: var(--glass-shadow);
            backdrop-filter: blur(var(--glass-blur));
            padding-top: 48px;
            padding-bottom: 48px;
            margin-bottom: 32px;
            border-bottom: 1px solid var(--glass-border);
        }
        .welcome-logo-container {
            width: 120px;
            height: 120px;
            border-radius: 50%;
            background: var(--glass-bg);
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0 auto 28px auto;
            box-shadow: 0 8px 32px rgba(31,38,135,0.12);
        }
        .welcome-logo {
            width: 80px;
            height: 80px;
            fill: var(--apple-blue);
        }
        .welcome-section h2 {
            font-size: 2em;
            font-weight: 700;
            color: var(--apple-dark);
            margin-bottom: 12px;
        }
        .welcome-section p {
            font-size: 1em;
            color: var(--apple-dark);
            line-height: 1.6;
            margin-bottom: 32px;
            max-width: 80%;
            margin-left: auto;
            margin-right: auto;
        }
        .welcome-quick-links {
            width: 100%;
            max-width: 400px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 32px;
        }
        .welcome-quick-link-btn {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 16px;
            padding: 18px 24px;
            display: flex;
            align-items: center;
            text-align: left;
            cursor: pointer;
            transition: background 0.2s, border-color 0.2s;
            box-shadow: 0 2px 8px rgba(31,38,135,0.08);
            backdrop-filter: blur(8px);
        }
        .welcome-quick-link-btn:hover {
            background: rgba(255,255,255,0.28);
            border-color: var(--apple-blue);
        }
        .welcome-quick-link-btn svg {
            width: 24px;
            height: 24px;
            fill: var(--apple-blue);
            margin-right: 15px;
        }
        .welcome-quick-link-content {
            flex-grow: 1;
        }
        .welcome-quick-link-content strong {
            display: block;
            font-size: 1.05em;
            font-weight: 600;
            color: var(--apple-dark);
            margin-bottom: 3px;
        }
        .welcome-quick-link-content span {
            font-size: 0.9em;
            color: var(--apple-blue);
        }
        .welcome-features-section {
            text-align: left;
            width: 100%;
            max-width: 400px;
            margin: 0 auto;
            padding-top: 24px;
        }
        .welcome-features-title {
            font-size: 1.05em;
            font-weight: 600;
            color: var(--apple-blue);
            margin-bottom: 18px;
        }
        .welcome-feature-item {
            display: flex;
            align-items: center;
            margin-bottom: 18px;
            font-size: 1em;
            color: var(--apple-dark);
        }
        .welcome-feature-item svg {
            width: 24px;
            height: 24px;
            margin-right: 15px;
            fill: var(--apple-blue);
        }

        .chat-section {
            padding-bottom: 24px;
        }
        .chat-header-chat {
            background: var(--glass-bg);
            color: var(--apple-blue);
            padding: 18px 24px;
            text-align: center;
            font-size: 1.15em;
            font-weight: 600;
            box-shadow: 0 2px 8px rgba(31,38,135,0.08);
            margin: 0 -32px 24px -32px;
            border-radius: var(--glass-radius);
            backdrop-filter: blur(8px);
        }
        .chat-header-chat p {
            margin: 0;
            font-size: 0.95em;
            font-weight: normal;
            opacity: 0.8;
            color: var(--apple-dark);
        }
        .chat-messages {
            display: flex;
            flex-direction: column;
            width: 100%;
            box-sizing: border-box;
        }
        .message-row {
            display: flex;
            margin-bottom: 18px;
            align-items: flex-start;
            width: 100%;
            box-sizing: border-box;
        }
        .message-icon {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-shrink: 0;
            font-size: 1em;
            font-weight: bold;
            color: var(--apple-light);
            margin: 0 12px;
            box-shadow: 0 2px 8px rgba(31,38,135,0.08);
        }
        .ai-icon {
            background: var(--apple-blue);
        }
        .user-icon {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            order: 2;
        }
        .message-row.user {
            justify-content: flex-end;
        }
        .message-row.user .message-bubble {
            margin-left: auto;
        }
        .message-bubble {
            padding: 14px 22px;
            border-radius: 28px;
            max-width: 78%;
            word-wrap: break-word;
            font-size: 1em;
            line-height: 1.6;
            box-shadow: 0 2px 8px rgba(31,38,135,0.08);
            position: relative;
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            backdrop-filter: blur(8px);
        }
        .ai-bubble {
            background: var(--glass-bg);
            color: var(--apple-dark);
            border-bottom-left-radius: 10px;
        }
        .user-bubble {
            background: var(--apple-blue);
            color: var(--apple-light);
            order: 1;
            border-bottom-right-radius: 10px;
        }
        .typing-indicator .message-bubble {
            background: var(--glass-bg);
            color: var(--apple-blue);
            font-style: italic;
            border-bottom-left-radius: 28px;
        }
        .message-bubble pre {
            white-space: pre-wrap;
            word-break: break-all;
            background: rgba(255,255,255,0.28);
            padding: 10px;
            border-radius: 8px;
            margin-top: 10px;
            margin-bottom: 10px;
            font-family: 'Consolas', 'Monaco', monospace;
            font-size: 0.95em;
            line-height: 1.5;
        }
        .message-bubble p {
            margin: 0 0 10px 0;
        }
        .message-bubble p:last-child {
            margin-bottom: 0;
        }
        .message-bubble ul, .message-bubble ol {
            padding-left: 28px;
            margin: 10px 0;
        }
        .message-bubble li {
            margin-bottom: 6px;
        }
        .message-bubble strong {
            font-weight: 700;
        }
        .message-bubble em {
            font-style: italic;
        }

        .input-area {
            flex-shrink: 0;
            width: 100%;
            display: flex;
            align-items: center;
            padding: 14px 24px;
            background: var(--glass-bg);
            border-top: 1px solid var(--glass-border);
            box-sizing: border-box;
            gap: 12px;
            backdrop-filter: blur(8px);
        }
        #userInput {
            flex-grow: 1;
            padding: 14px 22px;
            border: 1px solid var(--glass-border);
            border-radius: 28px;
            font-size: 1em;
            outline: none;
            transition: border-color 0.2s;
            background: var(--glass-bg);
            color: var(--apple-dark);
            box-shadow: 0 2px 8px rgba(31,38,135,0.08);
        }
        #userInput:focus {
            border-color: var(--apple-blue);
            background: rgba(255,255,255,0.28);
        }
        .chat-input-buttons {
            display: flex;
            gap: 8px;
        }
        .send-button, .mic-button {
            background: var(--apple-blue);
            border: none;
            border-radius: 50%;
            width: 48px;
            height: 48px;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            transition: background 0.2s;
            box-shadow: 0 2px 8px rgba(31,38,135,0.08);
        }
        .send-button:hover, .mic-button:hover {
            background: #0056b3;
        }
        .send-button:disabled, .mic-button:disabled {
            background: var(--glass-bg);
            cursor: not-allowed;
        }
        .send-button svg, .mic-button svg {
            fill: var(--apple-light);
            width: 24px;
            height: 24px;
        }
        .send-button#sendButton svg {
            transform: rotate(45deg);
        }

        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(255,255,255,0.18);
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(31,38,135,0.18);
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(31,38,135,0.28);
        }
        .hidden {
            display: none !important;
        }
    </style>
</head>
<body>
    <div class="app-container">
        <div class="header">
            <button class="header-icon-btn" id="menuButton">
                <svg viewBox="0 0 24 24">
                    <path d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z"/>
                </svg>
            </button>
            <h1 class="header-title">Health Assistant</h1>
            <div class="user-avatar">A</div>
        </div>

        <div class="sidebar" id="sidebar">
            <ul class="sidebar-menu">
                <li class="sidebar-menu-item" data-section="chat-section">
                    <svg viewBox="0 0 24 24">
                        <path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 9h12v2H6V9zm8 6H6v-2h8v2zm4-4H6V7h12v2z"/>
                    </svg>
                    Ask Health Questions
                </li>
            </ul>
            <div class="sidebar-divider"></div>
            <h3 class="sidebar-features-title">Key Features</h3>
            <ul class="sidebar-feature-list">
                <li class="sidebar-feature-list-item">Instant Health Answers</li>
                <li class="sidebar-feature-list-item">Symptom Analysis</li>
                <li class="sidebar-feature-list-item">Medical Terminology Clarification</li>
                <li class="sidebar-feature-list-item">Secure Information Handling</li>
            </ul>
        </div>

        <div class="overlay" id="overlay"></div>

        <div class="main-content-area" id="mainContentArea">
            <div class="welcome-section" id="welcomeSection">
                <div class="welcome-logo-container">
                    <svg class="welcome-logo" viewBox="0 0 24 24">
                        <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                    </svg>
                </div>
                <h2>Welcome to Your AI Health Assistant</h2>
                <p>Get instant answers to your health questions, analyze symptoms, and manage your medical information securely.</p>
                <div class="welcome-quick-links">
                    <button class="welcome-quick-link-btn" data-section="chat-section">
                        <svg viewBox="0 0 24 24">
                            <path d="M20 2H4c-1.1 0-1.99.9-1.99 2L2 22l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM6 9h12v2H6V9zm8 6H6v-2h8v2zm4-4H6V7h12v2z"/>
                        </svg>
                        <div class="welcome-quick-link-content">
                            <strong>Ask Health Questions</strong>
                            <span>Get instant AI-powered health guidance</span>
                        </div>
                    </button>
                </div>
                <div class="welcome-features-section">
                    <h3 class="welcome-features-title">Key Features</h3>
                    <div class="welcome-feature-item">
                        <svg viewBox="0 0 24 24">
                            <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                        </svg>
                        Instant Health Answers
                    </div>
                    <div class="welcome-feature-item">
                        <svg viewBox="0 0 24 24">
                            <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                        </svg>
                        Symptom Analysis
                    </div>
                    <div class="welcome-feature-item">
                        <svg viewBox="0 0 24 24">
                            <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                        </svg>
                        Medical Terminology Clarification
                    </div>
                    <div class="welcome-feature-item">
                        <svg viewBox="0 0 24 24">
                            <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                        </svg>
                        Secure Information Handling
                    </div>
                </div>
            </div>

            <div class="chat-section" id="chatSection">
                <div class="chat-header-chat">
                    Health Chat
                    <p>Get instant answers to your health questions</p>
                </div>
                <div class="chat-messages" id="chatMessages">
                    </div>
            </div>
        </div>

        <div class="input-area">
            <button class="send-button" id="plusButton">
                <svg viewBox="0 0 24 24">
                    <path d="M19 13h-6v6h-2v-6H5v-2h6V5h2v6h6v2z"/>
                </svg>
            </button>
            <input type="text" id="userInput" placeholder="Ask about symptoms, injuries...">
            <div class="chat-input-buttons">
                <button class="send-button" id="micButton">
                    <svg viewBox="0 0 24 24">
                        <path d="M12 14c1.66 0 2.99-1.34 2.99-3L15 5c0-1.66-1.34-3-3-3S9 3.34 9 5v6c0 1.66 1.34 3 3 3zm5.3-3c0 3.31-2.69 6-6 6s-6-2.69-6-6H4c0 3.98 3.5 7.29 8 7.94V21h2v-3.06c4.5-.65 8-3.96 8-7.94h-2.7z"/>
                    </svg>
                </button>
                <button class="send-button" id="sendButton">
                    <svg viewBox="0 0 24 24">
                        <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
                    </svg>
                </button>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const appContainer = document.querySelector('.app-container');
            const menuButton = document.getElementById('menuButton');
            const sidebar = document.getElementById('sidebar');
            const overlay = document.getElementById('overlay');
            const sidebarMenuItems = document.querySelectorAll('.sidebar-menu-item');
            const welcomeQuickLinks = document.querySelectorAll('.welcome-quick-link-btn');
            const mainContentArea = document.getElementById('mainContentArea'); // The new scrollable area

            const chatMessages = document.getElementById('chatMessages');
            const userInput = document.getElementById('userInput');
            const sendButton = document.getElementById('sendButton');
            const micButton = document.getElementById('micButton');
            const plusButton = document.getElementById('plusButton');

            // IMPORTANT: This URL points to your Flask backend on port 5000!
            const OLLAMA_BACKEND_URL = 'http://127.0.0.1:5000/api/generate-response';

            let currentTypingMessageRow = null;
            let abortController = null;

            // --- UI Navigation and Scroll Functions ---

            function openSidebar() {
                sidebar.classList.add('open');
                overlay.classList.add('active');
            }

            function closeSidebar() {
                sidebar.classList.remove('open');
                overlay.classList.remove('active');
            }

            // Function to scroll to a specific section (e.g., chat)
            function scrollToSection(sectionId) {
                const section = document.getElementById(sectionId);
                if (section) {
                    mainContentArea.scrollTo({
                        top: section.offsetTop,
                        behavior: 'smooth'
                    });
                }
                closeSidebar(); // Close sidebar after navigating
            }

            function autoScrollChatToBottom() {
                // Scroll the main content area to ensure the bottom of chat messages is visible
                mainContentArea.scrollTo({
                    top: mainContentArea.scrollHeight,
                    behavior: 'smooth'
                });
            }

            // --- Chat Specific Functions ---

            // Function to convert Markdown-like text to HTML for better display
            function formatMessageText(text) {
                // This is a basic markdown parser. For full robust markdown, consider a library.
                // Replace code blocks first to prevent inner formatting
                text = text.replace(/```([\s\S]*?)```/g, '<pre>$1</pre>');
                text = text.replace(/`(.*?)`/g, '<code>$1</code>');

                // Bold text: **text** or *text*
                text = text.replace(/\*\*(.*?)\*\*|\*(.*?)\*/g, '<strong>$1$2</strong>');
                // Italic text: _text_
                text = text.replace(/_(.*?)_/g, '<em>$1</em>');

                // Handle lists (basic, assumes list items are on new lines)
                // Convert list items to temporary placeholders before paragraph splitting
                text = text.replace(/^\s*[-*+]\s*(.*)$/gm, '<li>$1</li>'); // Unordered
                text = text.replace(/^\s*\d+\.\s*(.*)$/gm, '<li>$1</li>'); // Ordered

                // Group list items into ul/ol tags
                const listPattern = /(?:<li>.*?<\/li>\s*)+/g;
                text = text.replace(listPattern, (match) => {
                    if (match.trim().startsWith('<li>')) { // Simple check, could be more robust
                        // Determine if it's an ordered or unordered list by checking the original lines
                        // This might be tricky with just the `text` after replacements.
                        // A more reliable way is to process lines before joining.
                        // For simplicity, let's just make it an unordered list.
                        return `<ul>${match}</ul>`;
                    }
                    return match;
                });

                // Newlines to paragraphs, but avoid wrapping already processed blocks
                text = text.split('\n').map(line => {
                    const trimmedLine = line.trim();
                    if (trimmedLine === '' || trimmedLine.startsWith('<pre') || trimmedLine.startsWith('<code') || trimmedLine.startsWith('<ul') || trimmedLine.startsWith('<ol') || trimmedLine.startsWith('<li>') || trimmedLine.startsWith('<strong>') || trimmedLine.startsWith('<em>')) {
                        return line;
                    }
                    return `<p>${line}</p>`;
                }).join('');

                // Clean up any double paragraph tags or empty paragraph tags that might have resulted
                text = text.replace(/<p>\s*<\/p>/g, ''); // Remove empty paragraphs
                text = text.replace(/<p><(ul|ol|pre|code)/g, '<$1'); // Remove <p> before ul/ol/pre/code
                text = text.replace(/(ul|ol|pre|code)><\/p>/g, '$1>'); // Remove </p> after ul/ol/pre/code

                return text;
            }


            function createIconSVG(type) {
                if (type === 'ai') {
                    // Star Icon for AI (simplified for consistency)
                    return `<svg viewBox="0 0 24 24" fill="white" width="20px" height="20px">
                                <path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/>
                            </svg>`;
                } else {
                    // User Profile Icon
                    return `<svg viewBox="0 0 24 24" fill="white" width="20px" height="20px">
                                <path d="M12 12c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm0 2c-2.67 0-8 1.34-8 4v2h16v-2c0-2.66-5.33-4-8-4z"/>
                            </svg>`;
                }
            }

            function addMessageToChat(role, text, isTyping = false) {
                const messageRow = document.createElement('div');
                messageRow.classList.add('message-row');
                messageRow.classList.add(role === 'AI' ? 'ai' : 'user');

                const messageIcon = document.createElement('div');
                messageIcon.classList.add('message-icon');
                messageIcon.classList.add(role === 'AI' ? 'ai-icon' : 'user-icon');
                messageIcon.innerHTML = role === 'AI' ? createIconSVG('ai') : createIconSVG('user');

                const messageBubble = document.createElement('div');
                messageBubble.classList.add('message-bubble');
                messageBubble.classList.add(role === 'AI' ? 'ai-bubble' : 'user-bubble');

                if (isTyping) {
                    messageRow.classList.add('typing-indicator');
                    messageBubble.textContent = 'AI is thinking...';
                } else {
                    messageBubble.innerHTML = formatMessageText(text);
                }

                if (role === 'AI') {
                    messageRow.appendChild(messageIcon);
                    messageRow.appendChild(messageBubble);
                } else {
                    messageRow.appendChild(messageBubble);
                    messageRow.appendChild(messageIcon);
                }
                chatMessages.appendChild(messageRow);

                autoScrollChatToBottom(); // Auto-scroll whenever a new message is added

                if (isTyping) {
                    currentTypingMessageRow = messageRow;
                }
            }

            function updateStreamingMessage(textChunk) {
                if (currentTypingMessageRow) {
                    const messageBubble = currentTypingMessageRow.querySelector('.message-bubble');
                    if (messageBubble) {
                        if (currentTypingMessageRow.classList.contains('typing-indicator')) {
                            messageBubble.textContent = ''; // Clear "AI is thinking..."
                            currentTypingMessageRow.classList.remove('typing-indicator');
                            messageBubble.style.color = 'var(--dark-gray)'; // Reset color after typing
                        }
                        // Append raw chunk and then re-format the entire content
                        messageBubble.innerHTML += textChunk;
                        // Important: Re-parse and re-apply formatting to the entire current message content
                        // This helps correctly render markdown as it streams.
                        const currentRawText = messageBubble.textContent; // Get the raw text content
                        messageBubble.innerHTML = formatMessageText(currentRawText); // Re-render with formatting

                        autoScrollChatToBottom();
                    }
                }
            }


            function toggleInputFields(enabled) {
                userInput.disabled = !enabled;
                sendButton.disabled = !enabled;
                micButton.disabled = !enabled;
                plusButton.disabled = !enabled;
            }

            async function sendMessage() {
                const userText = userInput.value.trim();
                if (!userText) return;

                addMessageToChat('User', userText);
                userInput.value = '';

                addMessageToChat('AI', '', true); // Add typing indicator

                toggleInputFields(false);

                abortController = new AbortController();
                const signal = abortController.signal;

                try {
                    const response = await fetch(OLLAMA_BACKEND_URL, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ userInput: userText }),
                        signal: signal
                    });

                    if (!response.ok) {
                        let errorData;
                        try {
                            errorData = await response.json();
                        } catch (e) {
                            errorData = { error: `Server error: ${response.status} ${response.statusText}` };
                        }
                        throw new Error(errorData.error || `Server error: ${response.status} ${response.statusText}`);
                    }

                    const reader = response.body.getReader();
                    const decoder = new TextDecoder('utf-8');
                    let buffer = '';

                    while (true) {
                        const { value, done } = await reader.read();
                        if (done) {
                            break;
                        }
                        buffer += decoder.decode(value, { stream: true });

                        let lastNewlineIndex;
                        while ((lastNewlineIndex = buffer.indexOf('\n')) !== -1) {
                            const line = buffer.substring(0, lastNewlineIndex).trim();
                            buffer = buffer.substring(lastNewlineIndex + 1);

                            if (line.startsWith('data: ')) {
                                try {
                                    const jsonData = JSON.parse(line.substring(6));
                                    if (jsonData.token) {
                                        updateStreamingMessage(jsonData.token);
                                    }
                                    if (jsonData.done) {
                                        return;
                                    }
                                    if (jsonData.error) {
                                        throw new Error(jsonData.error);
                                    }
                                } catch (e) {
                                    console.error('Error parsing streaming JSON (SSE format):', e, line);
                                }
                            } else if (line) {
                                try {
                                    const jsonData = JSON.parse(line);
                                    if (jsonData.response) {
                                        updateStreamingMessage(jsonData.response);
                                    }
                                    if (jsonData.done) {
                                        return;
                                    }
                                    if (jsonData.error) {
                                        throw new Error(jsonData.error);
                                    }
                                } catch (e) {
                                    // Not JSON or malformed, ignore
                                }
                            }
                        }
                    }
                } catch (error) {
                    if (error.name === 'AbortError') {
                        console.log('Fetch request aborted.');
                    } else {
                        console.error('Fetch streaming error:', error);
                        if (currentTypingMessageRow) {
                            const messageBubble = currentTypingMessageRow.querySelector('.message-bubble');
                            if (messageBubble) {
                                let errorMessage = error.message || "An unexpected error occurred during streaming.";
                                if (errorMessage.includes('Server error initiating stream:') || errorMessage.includes('Failed to fetch')) {
                                    errorMessage = "Sorry, the AI service encountered an error or is not reachable. Please ensure Ollama and your backend are running.";
                                }
                                messageBubble.textContent = errorMessage; // Use textContent for error
                                messageBubble.style.color = 'red';
                                currentTypingMessageRow.classList.remove('typing-indicator');
                            }
                        } else {
                            addMessageToChat('AI', error.message || "An unexpected error occurred.");
                        }
                    }
                } finally {
                    toggleInputFields(true);
                    currentTypingMessageRow = null;
                    autoScrollChatToBottom(); // Ensure it scrolls to bottom after stream ends/errors
                    abortController = null;
                }
            }

            // --- Event Listeners ---

            // Sidebar and Overlay
            menuButton.addEventListener('click', openSidebar);
            overlay.addEventListener('click', closeSidebar);
            sidebarMenuItems.forEach(item => {
                item.addEventListener('click', (e) => {
                    const sectionId = e.currentTarget.dataset.section;
                    scrollToSection(sectionId);
                });
            });

            // Welcome page quick links
            welcomeQuickLinks.forEach(button => {
                button.addEventListener('click', (e) => {
                    const sectionId = e.currentTarget.dataset.section;
                    scrollToSection(sectionId);
                });
            });

            // Chat input and send
            sendButton.addEventListener('click', sendMessage);
            userInput.addEventListener('keypress', (e) => {
                if (e.key === 'Enter') {
                    sendMessage();
                }
            });

            // Initial chat message for the chat section (only once)
            const initialChatLoad = () => {
                if (!chatMessages.dataset.initialized) {
                    addMessageToChat('AI', "Hello! I'm your AI Health Assistant. I'm here to help answer your health questions and provide guidance. Please remember that I'm not a replacement for professional medical advice. How can I assist you today?");
                    chatMessages.dataset.initialized = 'true';
                }
            };

            // Call initial chat load when the DOM is ready
            initialChatLoad();
        });
    </script>
</body>
</html>
