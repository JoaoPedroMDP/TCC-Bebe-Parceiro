import { TestBed } from '@angular/core/testing';

import { ValidCodeGuard } from './valid-code.guard';

describe('ValidCodeGuard', () => {
  let guard: ValidCodeGuard;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    guard = TestBed.inject(ValidCodeGuard);
  });

  it('should be created', () => {
    expect(guard).toBeTruthy();
  });
});
