import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Manages persistent favorite projects using SharedPreferences.
class FavoritesService extends ChangeNotifier {
  static const _key = 'favorite_project_indices';
  static FavoritesService? _instance;
  static FavoritesService get instance => _instance!;

  List<int> _favorites = [];

  /// Initialize the service. Must be called once at app startup.
  static Future<FavoritesService> init() async {
    final prefs = await SharedPreferences.getInstance();
    final service = FavoritesService._();
    final raw = prefs.getStringList(_key) ?? [];
    service._favorites = raw.map((e) => int.tryParse(e) ?? -1).where((e) => e >= 0).toList();
    _instance = service;
    return service;
  }

  FavoritesService._();

  List<int> get favorites => List.unmodifiable(_favorites);

  bool isFavorite(int index) => _favorites.contains(index);

  int get count => _favorites.length;

  Future<void> toggleFavorite(int index) async {
    if (_favorites.contains(index)) {
      _favorites.remove(index);
    } else {
      _favorites.add(index);
    }
    await _persist();
    notifyListeners();
  }

  Future<void> _persist() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setStringList(_key, _favorites.map((e) => e.toString()).toList());
  }
}
