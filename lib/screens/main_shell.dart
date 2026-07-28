import 'package:flutter/material.dart';
import '../data/project_data.dart';
import 'home_screen.dart';
import 'projects_screen.dart';
import 'skills_explorer_screen.dart';
import 'contact_screen.dart';
import 'settings_screen.dart';
import 'project_detail_screen.dart';

class MainShell extends StatefulWidget {
  final ValueChanged<ThemeMode> onThemeChanged;
  final ValueChanged<String> onLanguageChanged;
  final ThemeMode currentThemeMode;
  final String currentLanguage;
  final int? initialDeepLinkProjectIndex;

  const MainShell({
    super.key,
    required this.onThemeChanged,
    required this.onLanguageChanged,
    required this.currentThemeMode,
    required this.currentLanguage,
    this.initialDeepLinkProjectIndex,
  });

  @override
  State<MainShell> createState() => _MainShellState();
}

class _MainShellState extends State<MainShell> {
  int _currentIndex = 0;
  final PageController _pageController = PageController();
  late ThemeMode _themeMode;
  late String _language;

  final List<_TabItem> _tabs = [
    _TabItem(icon: Icons.home_outlined, selectedIcon: Icons.home, label: 'Home'),
    _TabItem(icon: Icons.work_outline, selectedIcon: Icons.work, label: 'Projects'),
    _TabItem(icon: Icons.auto_awesome_outlined, selectedIcon: Icons.auto_awesome, label: 'Skills'),
    _TabItem(icon: Icons.mail_outline, selectedIcon: Icons.mail, label: 'Contact'),
    _TabItem(icon: Icons.settings_outlined, selectedIcon: Icons.settings, label: 'Settings'),
  ];

  @override
  void initState() {
    super.initState();
    _themeMode = widget.currentThemeMode;
    _language = widget.currentLanguage;

    // Handle deep link after first frame
    WidgetsBinding.instance.addPostFrameCallback((_) {
      final index = widget.initialDeepLinkProjectIndex;
      if (index != null && index >= 0 && index < ProjectData.allProjects.length) {
        _navigateToProjectDetail(index);
      }
    });
  }

  void _onTabTapped(int index) {
    setState(() => _currentIndex = index);
    _pageController.animateToPage(
      index,
      duration: const Duration(milliseconds: 300),
      curve: Curves.easeInOut,
    );
  }

  void _navigateToProjectDetail(int projectIndex) {
    final project = ProjectData.allProjects[projectIndex];
    Navigator.of(context).push(
      MaterialPageRoute(
        builder: (_) => ProjectDetailScreen(project: project),
      ),
    );
  }

  void _onThemeChanged(ThemeMode mode) {
    setState(() => _themeMode = mode);
    widget.onThemeChanged(mode);
  }

  void _onLanguageChanged(String lang) {
    setState(() => _language = lang);
    widget.onLanguageChanged(lang);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: PageView(
        controller: _pageController,
        onPageChanged: (index) => setState(() => _currentIndex = index),
        children: [
          HomeScreen(onProjectTap: _navigateToProjectDetail),
          ProjectsScreen(onProjectTap: _navigateToProjectDetail),
          const SkillsExplorerScreen(),
          const ContactScreen(),
          SettingsScreen(
            currentThemeMode: _themeMode,
            onThemeChanged: _onThemeChanged,
            currentLanguage: _language,
            onLanguageChanged: _onLanguageChanged,
          ),
        ],
      ),
      bottomNavigationBar: NavigationBar(
        selectedIndex: _currentIndex,
        onDestinationSelected: _onTabTapped,
        destinations: _tabs
            .map((tab) => NavigationDestination(
                  icon: Icon(tab.icon),
                  selectedIcon: Icon(tab.selectedIcon),
                  label: tab.label,
                ))
            .toList(),
      ),
    );
  }
}

class _TabItem {
  final IconData icon;
  final IconData selectedIcon;
  final String label;

  const _TabItem({
    required this.icon,
    required this.selectedIcon,
    required this.label,
  });
}
