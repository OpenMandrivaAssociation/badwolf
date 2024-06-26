# Work around incomplete debug packages
%global _empty_manifest_terminate_build 0

%define tarname badWolf

Name:		badwolf
Version:	1.3.0
Release:	2
Summary:	Web Browser which aims at security and privacy over usability
License:	BSD
URL:		https://hacktivis.me/projects/badwolf
#Source0:	https://gitlab.com/lanodan/badWolf/-/archive/v%{version}/%{tarname}-v%{version}.tar.bz2
Source0:  https://hacktivis.me/releases/badwolf-%{version}.tar.gz
BuildRequires:  ed
BuildRequires:  ninja
BuildRequires:	make
BuildRequires:	gettext
BuildRequires:	desktop-file-utils
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(webkit2gtk-4.1)
Requires:	hicolor-icon-theme

%description
BadWolf is a minimalist and privacy-oriented WebKitGTK+ browser.

- Privacy-oriented:
No browser-level tracking, multiple ephemeral isolated sessions per new
unrelated tabs, JavaScript off by default.

- Minimalist:
Small codebase (~1 500 LoC), reuses existing components when available or makes
it available.

- Customizable:
WebKitGTK native extensions, Interface customizable through CSS.

- Powerful & Usable:
Stable User-Interface; The common shortcuts are available (and documented), no
vi-modal edition or single-key shortcuts are used.

- No annoyances:
Dialogs are only used when required (save file, print, …), javascript popups
open in a background tab.


%prep
%autosetup -n %{name}-%{version}

%build
PREFIX=%{_prefix} ./configure
%ninja_build

%install
%ninja_install
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}

%find_lang Badwolf

%files -f Badwolf.lang
%license COPYING
%doc README.md KnowledgeBase.md
%{_bindir}/badwolf
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/locale
%dir %{_datadir}/%{name}/locale/*
%dir %{_datadir}/%{name}/locale/*/LC_MESSAGES
%{_datadir}/%{name}/interface.css
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_mandir}/man1/%{name}.1.*
%{_mandir}/*/man1/badwolf.1.*
