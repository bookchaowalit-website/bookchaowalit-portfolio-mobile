import 'package:flutter/material.dart';
import '../data/project_data.dart';
import '../services/favorites_service.dart';
import '../widgets/section_header.dart';
import '../widgets/project_card.dart';

class ProjectsScreen extends StatefulWidget {
  final ValueChanged<int> onProjectTap;

  const ProjectsScreen({super.key, required this.onProjectTap});

  @override
  State<ProjectsScreen> createState() => _ProjectsScreenState();
}

class _ProjectsScreenState extends State<ProjectsScreen> {
  final _searchController = TextEditingController();
  String _searchQuery = '';
  bool _showFavoritesOnly = false;

  late final FavoritesService _favService;

  @override
  void initState() {
    super.initState();
    _favService = FavoritesService.instance;
    _favService.addListener(_onFavoritesChanged);
  }

  @override
  void dispose() {
    _searchController.dispose();
    _favService.removeListener(_onFavoritesChanged);
    super.dispose();
  }

  void _onFavoritesChanged() {
    if (mounted) setState(() {});
  }

  List<int> get _filteredIndices {
    final projects = ProjectData.allProjects;
    var indices = List<int>.generate(projects.length, (i) => i);

    // Filter by favorites
    if (_showFavoritesOnly) {
      indices = indices.where((i) => _favService.isFavorite(i)).toList();
    }

    // Filter by search
    if (_searchQuery.isNotEmpty) {
      final q = _searchQuery.toLowerCase();
      indices = indices.where((i) {
        final p = projects[i];
        return p.name.toLowerCase().contains(q) ||
            p.description.toLowerCase().contains(q) ||
            p.tags.any((t) => t.toLowerCase().contains(q));
      }).toList();
    }

    return indices;
  }

  @override
  Widget build(BuildContext context) {
    final colorScheme = Theme.of(context).colorScheme;
    final filteredIndices = _filteredIndices;

    return CustomScrollView(
      physics: const AlwaysScrollableScrollPhysics(),
      slivers: [
        // Header
        SliverToBoxAdapter(
          child: Container(
            padding: const EdgeInsets.fromLTRB(24, 60, 24, 16),
            decoration: BoxDecoration(
              gradient: LinearGradient(
                begin: Alignment.topCenter,
                end: Alignment.bottomCenter,
                colors: [
                  colorScheme.primaryContainer.withValues(alpha: 0.2),
                  colorScheme.surface,
                ],
              ),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SectionHeader(title: 'Projects'),
                const SizedBox(height: 8),
                Text(
                  'A selection of projects I\'ve built — from web apps to mobile and automation tools.',
                  style: Theme.of(context).textTheme.bodyLarge?.copyWith(
                        color: colorScheme.onSurfaceVariant,
                      ),
                ),
                const SizedBox(height: 16),

                // Search bar
                TextField(
                  controller: _searchController,
                  onChanged: (v) => setState(() => _searchQuery = v),
                  decoration: InputDecoration(
                    hintText: 'Search projects, tags...',
                    prefixIcon: const Icon(Icons.search, size: 20),
                    suffixIcon: _searchQuery.isNotEmpty
                        ? IconButton(
                            icon: const Icon(Icons.clear, size: 18),
                            onPressed: () {
                              _searchController.clear();
                              setState(() => _searchQuery = '');
                            },
                          )
                        : null,
                    filled: true,
                    fillColor: colorScheme.surfaceContainerHighest.withValues(alpha: 0.5),
                    border: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(12),
                      borderSide: BorderSide.none,
                    ),
                    contentPadding: const EdgeInsets.symmetric(
                        horizontal: 16, vertical: 12),
                    isDense: true,
                  ),
                ),
                const SizedBox(height: 12),

                // Filter chips row
                Row(
                  children: [
                    FilterChip(
                      label: Text(
                        'All (${ProjectData.allProjects.length})',
                        style: const TextStyle(fontSize: 12),
                      ),
                      selected: !_showFavoritesOnly,
                      onSelected: (_) =>
                          setState(() => _showFavoritesOnly = false),
                    ),
                    const SizedBox(width: 8),
                    FilterChip(
                      label: Text(
                        'Favorites (${_favService.count})',
                        style: const TextStyle(fontSize: 12),
                      ),
                      selected: _showFavoritesOnly,
                      onSelected: (_) =>
                          setState(() => _showFavoritesOnly = true),
                      avatar: Icon(
                        Icons.favorite,
                        size: 16,
                        color: _showFavoritesOnly
                            ? colorScheme.primary
                            : colorScheme.onSurfaceVariant,
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),

        // Project Cards
        if (filteredIndices.isEmpty)
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(24, 48, 24, 48),
              child: Column(
                children: [
                  Icon(
                    _showFavoritesOnly
                        ? Icons.favorite_border
                        : Icons.search_off,
                    size: 48,
                    color: colorScheme.onSurfaceVariant.withValues(alpha: 0.4),
                  ),
                  const SizedBox(height: 16),
                  Text(
                    _showFavoritesOnly
                        ? 'No favorite projects yet.\nTap the heart icon on any project to save it.'
                        : 'No projects match "$_searchQuery"',
                    textAlign: TextAlign.center,
                    style: Theme.of(context).textTheme.bodyMedium?.copyWith(
                          color: colorScheme.onSurfaceVariant,
                        ),
                  ),
                ],
              ),
            ),
          )
        else
          SliverToBoxAdapter(
            child: Padding(
              padding: const EdgeInsets.fromLTRB(24, 16, 24, 0),
              child: Column(
                children: filteredIndices.map((index) {
                  final p = ProjectData.allProjects[index];
                  return _AnimatedProjectCard(
                    name: p.name,
                    description: p.description,
                    tags: p.tags,
                    url: p.url,
                    isFavorite: _favService.isFavorite(index),
                    onTap: () => widget.onProjectTap(index),
                    onFavoriteToggle: () => _favService.toggleFavorite(index),
                  );
                }).toList(),
              ),
            ),
          ),

        const SliverToBoxAdapter(child: SizedBox(height: 24)),
      ],
    );
  }
}

class _AnimatedProjectCard extends StatelessWidget {
  final String name;
  final String description;
  final List<String> tags;
  final String url;
  final bool isFavorite;
  final VoidCallback onTap;
  final VoidCallback onFavoriteToggle;

  const _AnimatedProjectCard({
    required this.name,
    required this.description,
    required this.tags,
    required this.url,
    required this.isFavorite,
    required this.onTap,
    required this.onFavoriteToggle,
  });

  @override
  Widget build(BuildContext context) {
    return TweenAnimationBuilder<double>(
      tween: Tween(begin: 0.0, end: 1.0),
      duration: const Duration(milliseconds: 500),
      curve: Curves.easeOut,
      builder: (context, value, child) {
        return Opacity(
          opacity: value,
          child: Transform.translate(
            offset: Offset(0, 15 * (1 - value)),
            child: Padding(
              padding: const EdgeInsets.only(bottom: 12),
              child: child,
            ),
          ),
        );
      },
      child: ProjectCard(
        name: name,
        description: description,
        tags: tags,
        url: url,
        isFavorite: isFavorite,
        onTap: onTap,
        onFavoriteToggle: onFavoriteToggle,
      ),
    );
  }
}
