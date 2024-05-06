import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListSwapComponent } from './list-swap.component';

describe('ListSwapComponent', () => {
  let component: ListSwapComponent;
  let fixture: ComponentFixture<ListSwapComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListSwapComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListSwapComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
