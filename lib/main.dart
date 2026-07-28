import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:app_links/app_links.dart';
import 'screens/splash_screen.dart';
import 'services/favorites_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  // Load saved preferences
  final prefs = await SharedPreferences.getInstance();
  final themeIndex = prefs.getInt('theme_mode') ?? 0;
  final language = prefs.getString('language') ?? 'en';

  // Initialize favorites persistence
  await FavoritesService.init();

  runApp(BookChaowalitPortfolioApp(
    initialThemeMode: ThemeMode.values[themeIndex],
    initialLanguage: language,
  ));
}

class BookChaowalitPortfolioApp extends StatefulWidget {
  final ThemeMode initialThemeMode;
  final String initialLanguage;

  const BookChaowalitPortfolioApp({
    super.key,
    required this.initialThemeMode,
    required this.initialLanguage,
  });

  @override
  State<BookChaowalitPortfolioApp> createState() => _BookChaowalitPortfolioAppState();
}

class _BookChaowalitPortfolioAppState extends State<BookChaowalitPortfolioApp> {
  late ThemeMode _themeMode;
  late String _language;
  SharedPreferences? _prefs;

  @override
  void initState() {
    super.initState();
    _themeMode = widget.initialThemeMode;
    _language = widget.initialLanguage;
    _initPrefsAndDeepLinks();
  }

  final AppLinks _appLinks = AppLinks();

  Future<void> _initPrefsAndDeepLinks() async {
    _prefs = await SharedPreferences.getInstance();
    // Listen for deep links
    _appLinks.uriLinkStream.listen((Uri uri) {
      if (mounted) {
        _handleDeepLink(uri);
      }
    });
    // Handle initial deep link
    try {
      final initialUri = await _appLinks.getInitialLink();
      if (initialUri != null && mounted) {
        _handleDeepLink(initialUri);
      }
    } catch (_) {}
  }

  void _handleDeepLink(Uri uri) {
    // Deep link format: https://bookchaowalit.com/project/<index>
    // or: bookchaowalit://project/<index>
    final pathSegments = uri.pathSegments;
    if (pathSegments.length >= 2 && pathSegments[0] == 'project') {
      final index = int.tryParse(pathSegments[1]);
      if (index != null) {
        // Navigate will be handled by MainShell via the navigator key
        // For now, store the pending deep link index
        _pendingDeepLinkIndex = index;
      }
    }
  }

  int? _pendingDeepLinkIndex;
  int? get pendingDeepLinkIndex => _pendingDeepLinkIndex;
  void clearPendingDeepLink() => _pendingDeepLinkIndex = null;

  void _onThemeChanged(ThemeMode mode) {
    setState(() => _themeMode = mode);
    _prefs?.setInt('theme_mode', mode.index);
  }

  void _onLanguageChanged(String lang) {
    setState(() => _language = lang);
    _prefs?.setString('language', lang);
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Chaowalit Greepoke Portfolio',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.black,
          brightness: Brightness.light,
        ),
        useMaterial3: true,
        textTheme: GoogleFonts.interTextTheme(),
      ),
      darkTheme: ThemeData(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.white,
          brightness: Brightness.dark,
        ),
        useMaterial3: true,
        textTheme: GoogleFonts.interTextTheme(ThemeData.dark().textTheme),
      ),
      themeMode: _themeMode,
      home: SplashScreen(
        onThemeChanged: _onThemeChanged,
        onLanguageChanged: _onLanguageChanged,
        currentThemeMode: _themeMode,
        currentLanguage: _language,
        getPendingDeepLink: () => pendingDeepLinkIndex,
        clearPendingDeepLink: clearPendingDeepLink,
      ),
    );
  }
}
