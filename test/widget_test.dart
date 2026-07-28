import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:bookchaowalit_portfolio_mobile/screens/home_screen.dart';
import 'package:bookchaowalit_portfolio_mobile/services/favorites_service.dart';

void main() {
  testWidgets('Home screen displays hero content', (WidgetTester tester) async {
    SharedPreferences.setMockInitialValues({});
    await FavoritesService.init();

    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: HomeScreen(onProjectTap: (_) {}),
        ),
      ),
    );

    // Verify hero content (visible above the fold)
    expect(find.text('Chaowalit Greepoke'), findsOneWidget);
    expect(find.text('Generalist & Solopreneur'), findsOneWidget);
    expect(find.text('Hire Me'), findsOneWidget);
    expect(find.text('Website'), findsOneWidget);
  });
}
